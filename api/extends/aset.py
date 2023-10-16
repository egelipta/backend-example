# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: Aset Management
"""
from core.Response import success, fail, res_antd
from models.aset import Aset
from models.merek_tipe import MerekTipe
from models.lokasi import Lokasi
from models.power import Power
from fastapi import Request, Query, APIRouter, File
from tortoise.queryset import F
from schemas import aset, pakai_aset

#--------------------------------------------------
import os
from datetime import datetime, date
from fastapi.responses import FileResponse
from models.aset import Aset


router = APIRouter(prefix='/aset')

# @router.get("" summary="Akses Ruangan")
# async def aksesRuangan(

# ):
#     akses_ruangan = await Device.fi


@router.post("", summary="Aset Add",
             )
async def aset_add(post: aset.CreateAset):
    """
    Aset Add
    :param post: CreateAset
    :return:
    """
    
    get_aset_nomor_seri = await Aset.get_or_none(nomor_seri=post.nomor_seri)
    get_merek_tipe = await MerekTipe.get_or_none(merek=post.merek, tipe=post.tipe)
    get_lokasi = await Lokasi.get_or_none(lokasi=post.lokasi, nama_ruangan=post.nama_ruangan, posisi_rak=post.posisi_rak, posisi_u=post.posisi_u)

    # get_aset_data_pengunjung = await Aset.get_or_none(data_pengunjung=post.data_pengunjung])
    # get_aset_akses_ruangan = await Aset.get_or_none(akses_ruangan=post.akses_ruangan)
    # get_aset_nama_pic = await Aset.get_or_none(nama_pic=post.nama_pic)
    # get_aset_nip_pic = await Aset.get_or_none(nip_pic=post.nip_pic)
    # get_aset_keperluan = await Aset.get_or_none(keperluan=post.keperluan)
    # get_aset_mulai_kunjungan = await Aset.get_or_none(mulai_kunjungan=post.mulai_kunjungan)
    # get_aset_selesai_kunjungan = await Aset.get_or_none(selesai_kunjungan=post.selesai_kunjungan)
    # get_aset_data_pengunjung = await Aset.get_or_none(data_pengunjung=post.data_pengunjung)
    # get_aset_name = await Aset.get_or_none(name=post.name).filter(type=1)

    if get_aset_nomor_seri:
        return fail(msg=f"Seri/Model {post.nomor_seri} is exist!")

    if not get_merek_tipe:
        await MerekTipe.create(merek=post.merek, tipe=post.tipe)
    
    if not get_lokasi:
        await Lokasi.create(lokasi=post.lokasi, nama_ruangan=post.nama_ruangan, posisi_rak=post.posisi_rak, posisi_u=post.posisi_u, sn_aset=post.nomor_seri)

    if get_lokasi:
        await Lokasi.filter(lokasi=post.lokasi, nama_ruangan=post.nama_ruangan, posisi_rak=post.posisi_rak, posisi_u=post.posisi_u).update(sn_aset=post.nomor_seri)



    # Add Aset
    create_aset = await Aset.create(**post.dict())
    if not create_aset:
        return fail(msg=f"Failed to create Access {post.nomor_seri}!")
    return success(msg=f"Aset {create_aset.nomor_seri} created successfully")


@router.delete("aset-tmp", summary="Aset Delete"
               # dependencies=[Security(check_permissions, scopes=["aset_delete"])]
               )
async def aset_del_tmp(req: Request, user: str):
    """
    Aset Delete
    :param req:
    :return:
    """
    aset = await Aset.filter(user=user, status_aset=2)
       
    if not aset:
        return fail(msg="Cancel!")

    for x in range(len(aset)):
        await Power.filter(sn_aset=aset[x].nomor_seri ).update(sn_aset='kosong')
        await Lokasi.filter(sn_aset=aset[x].nomor_seri ).update(sn_aset='kosong')
        await Aset.filter(pk=aset[x].pk).delete()



@router.put("", summary="Update Aset"
            # dependencies=[Security(check_permissions, scopes=["aset_update"])]
            )
async def aset_update(post: aset.UpdateAset):
    """
    Update aset information
    :return:
    :param post:
    """
    aset_check = await Aset.get_or_none(pk=post.id)
    if not aset_check:
        return fail(msg="Aset does not exist")

    data = post.dict()
    data.pop("id")
    await Aset.filter(pk=post.id).update(**data)
    return success(msg="Updated!")


@router.get("",
            summary="Aset List",
            response_model=aset.AsetListData,
            # dependencies=[
            #     Security(check_permissions, scopes=["aset_query"])]
            )
async def aset_list(
        pageSize: int = 10,
        current: int = 1,
        merek: str = Query(None),
        tipe: str = Query(None),
        fungsi_perangkat: str = Query(None),
        foto_perangkat: str = Query(None),
        nomor_seri: str = Query(None),
        jenis_infra: str = Query(None),
        instansi_pemilik: str = Query(None),
        penanggung_jawab: int = Query(None),
        lokasi: str = Query(None),
        nama_ruangan: str = Query(None),
        posisi_rak: str = Query(None),
        psu: str = Query(None),
        posisi_u: str = Query(None),
        power: str = Query(None),
       
        kapasitas_cpu: str = Query(None),
        kapasitas_hdd: str = Query(None),
        kapasitas_ram: str = Query(None),
        daya: str = Query(None),
        tanggal_pemasangan: datetime = Query(None),
        tanggal_penarikan: str = Query(None),
        keterangan: str = Query(None),
        status_aset: bool = Query(True),
        create_time: str = Query(None),
        update_time: str = Query(None),
        user: str = Query(None),



):
    """
    Get All Asets
    :return:
    """
    # Query Conditions
    query = {}
    if merek:
        query.setdefault('merek', merek)
    if tipe:
        query.setdefault('tipe', tipe)
    if fungsi_perangkat:
        query.setdefault('fungsi_perangkat', fungsi_perangkat)
    if foto_perangkat:
        query.setdefault('foto_perangkat', foto_perangkat)
    if nomor_seri:
        query.setdefault('nomor_seri', nomor_seri)
    if jenis_infra:
        query.setdefault('jenis_infra', jenis_infra)
    if instansi_pemilik:
        query.setdefault('instansi_pemilik', instansi_pemilik)
    if penanggung_jawab:
        query.setdefault('penanggung_jawab', penanggung_jawab)
    if lokasi:
        query.setdefault('lokasi', lokasi)
    if nama_ruangan:
        query.setdefault('nama_ruangan', nama_ruangan)
    if posisi_rak:
        query.setdefault('posisi_rak', posisi_rak)
    if psu:
        query.setdefault('psu', psu)
    if posisi_u:
        query.setdefault('posisi_u', posisi_u)
    if power:
        query.setdefault('power_a', power)
    
    if kapasitas_cpu:
        query.setdefault('kapasitas_cpu', kapasitas_cpu)
    if kapasitas_hdd:
        query.setdefault('kapasitas_hdd', kapasitas_hdd)
    if kapasitas_ram:
        query.setdefault('kapasitas_ram', kapasitas_ram)
    if daya:
        query.setdefault('daya', daya)
    if tanggal_pemasangan:
        query.setdefault('tanggal_pemasangan', tanggal_pemasangan)
    if tanggal_penarikan:
        query.setdefault('tanggal_penarikan', tanggal_penarikan)
    if keterangan:
        query.setdefault('keterangan', keterangan)
    if status_aset:
        query.setdefault('status_aset', status_aset)
    if create_time:
        query.setdefault('create_time__range', create_time)
    if update_time:
        query.setdefault('update_time__range', update_time)
    if user:
        query.setdefault('user', user)
   

    aset_data = Aset.annotate(key=F("id")).filter(**query).all()
    print("aset_data: ", aset_data)
    # Total
    total = await aset_data.count()
    print("Total: ", total)
    # Query
    data = await aset_data.limit(pageSize).offset(pageSize * (current - 1)).order_by("-create_time") \
        .values(
        "key",
        "id",
        "merek",
        "tipe",
        "fungsi_perangkat",
        "foto_perangkat",
        "nomor_seri",
        "jenis_infra",
        "instansi_pemilik",
        "penanggung_jawab",
        "lokasi",
        "nama_ruangan",
        "posisi_rak",
        "psu",
        "posisi_u",
        "power",
        "user",
        "kapasitas_cpu",
        "kapasitas_hdd",
        "kapasitas_ram",
        "daya",
        "tanggal_pemasangan",
        "tanggal_penarikan",
        "keterangan",
        "status_aset",
        "create_time",
        "update_time",)
    
    print("DATA:", data)

    # Tambahkan jalur lengkap untuk setiap gambar yang akan ditampilkan
    for item in data:
        if item["foto_perangkat"]:
            item["foto_perangkat"] = os.path.join("static", "upload", "photo", item["foto_perangkat"])

    return res_antd(code=True, data=data, total=total)

@router.get("/upload/photo/{file_name}")
async def get_photo(file_name: str):
    # Konstruksi jalur lengkap menuju file gambar
    photo_path = os.path.join("static", "upload", "photo", file_name)

    # Periksa apakah file gambar ada atau tidak
    if not os.path.exists(photo_path):
        # File tidak ditemukan, kembalikan tanggapan kesalahan atau foto default jika ada
        default_photo_path = os.path.join("static", "upload", "photo", "default.jpg")
        return FileResponse(default_photo_path)

    # Kirimkan file gambar ke klien
    return FileResponse(photo_path)


@router.get("/dataPerangkat", summary="Data Perangkat")
async def dataPerangkat(req: Request, user: str):
    data_perangkat = await Aset.filter(status_aset=1, user=user).values('merek', 'tipe', 'nomor_seri')

    if data_perangkat:
        new_dict = {}
        for item in data_perangkat:
            id = item['nomor_seri']
            new_dict[id] = f"{item['merek']} / {item['tipe']} / {item['nomor_seri']}"

        result = new_dict.items()
        return success(data=result)
    else:
        return fail(msg="Data Perangkat Not Found!")


@router.put("/update-status", summary="Update Aset Status")
async def update_status_aset(post: aset.UpdateStatusAset):
    
    aset = await Aset.get_or_none(pk=post.id)
    seria_aset = aset.nomor_seri
    if not aset:
        return fail(msg="Aset does not exist")
        

    aset.status_aset = post.status_aset
    aset.tanggal_penarikan = datetime.now()
    await aset.save()

    await Power.filter(sn_aset=seria_aset ).update(sn_aset='kosong')
    await Lokasi.filter(sn_aset=seria_aset ).update(sn_aset='kosong')

    return success(msg="Aset Updated Successfully!")



@router.get("/status-false", summary="Aset List with Status False")
async def aset_list_with_status_false(
    pageSize: int = 10,
    current: int = 1,
):
    """
    Get All Asets with status_aset=False
    :return:
    """
    # Query Conditions
    query = {"status_aset": False}

    aset_data = Aset.annotate(key=F("id")).filter(**query).all()

    # Total
    total = await aset_data.count()

    # Query
    data = await aset_data.limit(pageSize).offset(pageSize * (current - 1)).order_by("-create_time") \
        .values(
        "key",
        "id",
        "merek",
        "tipe",
        "fungsi_perangkat",
        "foto_perangkat",
        "nomor_seri",
        "jenis_infra",
        "instansi_pemilik",
        "penanggung_jawab",
        "lokasi",
        "nama_ruangan",
        "posisi_rak",
        "psu",
        "posisi_u",
        "power",
        "user",
        "kapasitas_cpu",
        "kapasitas_hdd",
        "kapasitas_ram",
        "daya",
        "tanggal_pemasangan",
        "tanggal_penarikan",
        "keterangan",
        "status_aset",
        "create_time",
        "update_time",
    )

    # Tambahkan jalur lengkap untuk setiap gambar yang akan ditampilkan
    for item in data:
        if item["foto_perangkat"]:
            item["foto_perangkat"] = os.path.join("static", "upload", "photo", item["foto_perangkat"])

    return res_antd(code=True, data=data, total=total)

@router.get("/status-tmp", summary="Aset List with Status False")
async def aset_list_with_status_tmp(
    pageSize: int = 10,
    current: int = 1,
    status_aset: int = Query(None),
    user: str = Query(None),



):
    """
    Get All Asets with status_aset=False
    :return:
    """
    # Query Conditions
    query = {}
    if status_aset:
            query.setdefault('status_aset', status_aset)
    if user:
            query.setdefault('user', user)
       

    aset_data = Aset.annotate(key=F("id")).filter(**query).all()

    # Total
    total = await aset_data.count()

    # Query
    data = await aset_data.limit(pageSize).offset(pageSize * (current - 1)).order_by("-create_time") \
        .values(
        "key",
        "id",
        "merek",
        "tipe",
        "fungsi_perangkat",
        "foto_perangkat",
        "nomor_seri",
        "jenis_infra",
        "instansi_pemilik",
        "penanggung_jawab",
        "lokasi",
        "nama_ruangan",
        "posisi_rak",
        "psu",
        "posisi_u",
        "power",
        "user",
        "kapasitas_cpu",
        "kapasitas_hdd",
        "kapasitas_ram",
        "daya",
        "tanggal_pemasangan",
        "tanggal_penarikan",
        "keterangan",
        "status_aset",
        "create_time",
        "update_time",
    )

    # Tambahkan jalur lengkap untuk setiap gambar yang akan ditampilkan
    for item in data:
        if item["foto_perangkat"]:
            item["foto_perangkat"] = os.path.join("static", "upload", "photo", item["foto_perangkat"])

    return res_antd(code=True, data=data, total=total)

@router.put("book-status",
             summary="status-book",
            #  dependencies=[Security(check_permissions, scopes=["pengunjung_hadir_add"])]
             )
async def book_status_put(post: pakai_aset.InsertAkanPakaiAset):
    """
    PengunjungHadir Add
    :param post: CreatePengunjungHadir
    :return:
    """
    # Filter PengunjungHadirs
    # get_pengunjung_hadir_no_tiket = await PengunjungHadir.get_or_none(nomor_tiket=post.nomor_tiket[0])

    # if not get_pengunjung_hadir_no_tiket:
    #     return fail(msg=f" No tiket tidak ditemukan!")

    # post.password = en_password(post.password)

    # Add User
    
    ns = post.nomor_seri
    print(len(ns))
   
    for x in range(len(ns)):
        await Aset.filter(nomor_seri=ns[x]).update(status_aset=3)
            

    return success(msg=f"Sukses")

