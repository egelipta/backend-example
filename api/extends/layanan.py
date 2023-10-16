# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: Layanan Management
"""
from datetime import datetime
import os
import time

from api.endpoints.common import write_access_log
from api.extends.sms import check_code
from core.Response import success, fail, res_antd
from models.layanan import Layanan
from core.Utils import en_password, check_password, random_str
from core.Auth import create_access_token, check_permissions
from fastapi import Request, Query, APIRouter, Security, File, UploadFile
from config import settings
from typing import List
from tortoise.queryset import F
from tortoise.expressions import Q
from schemas import layanan
from fastapi.responses import FileResponse


router = APIRouter(prefix='/layanan')

# @router.get("" summary="Akses Ruangan")
# async def aksesRuangan(

# ):
#     akses_ruangan = await Device.fi


@router.post("", summary="Layanan Add",
             )
async def layanan_add(post: layanan.CreateLayanan):
    """
    Layanan Add
    :param post: CreateLayanan
    :return:
    """
    
    get_layanan_nomor_tiket = await Layanan.get_or_none(nomor_tiket=post.nomor_tiket)
    # get_layanan_data_pengunjung = await Layanan.get_or_none(data_pengunjung=post.data_pengunjung])
    # get_layanan_akses_ruangan = await Layanan.get_or_none(akses_ruangan=post.akses_ruangan)
    # get_layanan_nama_pic = await Layanan.get_or_none(nama_pic=post.nama_pic)
    # get_layanan_nip_pic = await Layanan.get_or_none(nip_pic=post.nip_pic)
    # get_layanan_keperluan = await Layanan.get_or_none(keperluan=post.keperluan)
    # get_layanan_mulai_kunjungan = await Layanan.get_or_none(mulai_kunjungan=post.mulai_kunjungan)
    # get_layanan_selesai_kunjungan = await Layanan.get_or_none(selesai_kunjungan=post.selesai_kunjungan)
    # get_layanan_data_pengunjung = await Layanan.get_or_none(data_pengunjung=post.data_pengunjung)
    # get_layanan_name = await Layanan.get_or_none(name=post.name).filter(type=1)

    if get_layanan_nomor_tiket:
        return fail(msg=f"Nomor Tiket {post.nomor_tiket} is exist!")

    # if get_layanan_akses_ruangan:
    #     # payload =
    #     str = ""
    #     for item in get_layanan_akses_ruangan:
    #         str + ";" + item

    # bakal_disimpan = post.dict()
    # bakal_disimpan['data_pengunjung'] = str(id_pengunjung)
    # bakal_disimpan['akses_ruangan'] = str(id_ruangan)
    # print("Bentuk data:", bakal_disimpan)

    # Add Layanan
    create_layanan = await Layanan.create(**post.dict())
    if not create_layanan:
        return fail(msg=f"Failed to create Access {post.nomor_tiket}!")
    return success(msg=f"Request Layanan {create_layanan.nomor_tiket} created successfully")


@router.delete("", summary="Layanan Delete"
               # dependencies=[Security(check_permissions, scopes=["layanan_delete"])]
               )
async def layanan_del(req: Request, id: int):
    """
    Layanan Delete
    :param req:
    :return:
    """
    layanan = await Layanan.get_or_none(pk=id)
    if not layanan:
        return fail(msg="ID does not exist!")
    result = await Layanan.filter(pk=id).delete()
    if not result:
        return fail(msg="failed to delete!")
    return success(msg="successfully deleted!")


@router.put("", summary="Update Layanan"
            # dependencies=[Security(check_permissions, scopes=["layanan_update"])]
            )
async def layanan_update(post: layanan.UpdateLayanan):
    """
    Update layanan information
    :return:
    :param post:
    """
    layanan_check = await Layanan.get_or_none(pk=post.id)
    if not layanan_check:
        return fail(msg="Layanan does not exist")
    if layanan_check.nomor_tiket != post.nomor_tiket:
        check = await Layanan.get_or_none(nomor_tiket=post.nomor_tiket)
        if check:
            return fail(msg=f"Layanan nomor_tiket {check.nomor_tiket} exist!")

    data = post.dict()
    data.pop("id")
    await Layanan.filter(pk=post.id).update(**data)
    return success(msg="Updated!")


@router.get("",
            summary="Layanan List",
            response_model=layanan.LayananListData,
            # dependencies=[
            #     Security(check_permissions, scopes=["layanan_query"])]
            )
async def layanan_list(
        pageSize: int = 10,
        current: int = 1,
        nomor_tiket: str = Query(None),
        jenis_layanan: str = Query(None),
        co_location: str = Query(None),
        # jenis_infra: str = Query(None),
        perangkat: str = Query(None),
        mulai_kunjungan: datetime = Query(None),
        akhir_kunjungan: int = Query(None),
        pemandu: str = Query(None),
        create_time: str = Query(None),
        update_time: str = Query(None),


):
    """
    Get All Layanans
    :return:
    """
    # Query Conditions
    query = {}
    if nomor_tiket:
        query.setdefault('nomor_tiket', nomor_tiket)
    if jenis_layanan:
        query.setdefault('jenis_layanan', jenis_layanan)
    if co_location:
        query.setdefault('co_location', co_location)
    # if jenis_infra:
    #     query.setdefault('jenis_infra', jenis_infra)
    if perangkat:
        query.setdefault('perangkat', perangkat)
    if mulai_kunjungan:
        query.setdefault('mulai_kunjungan__range', mulai_kunjungan)
    if akhir_kunjungan:
        query.setdefault('akhir_kunjungan', akhir_kunjungan)
    if pemandu:
        query.setdefault('pemandu', pemandu)
    if create_time:
        query.setdefault('create_time__range', create_time)
    if update_time:
        query.setdefault('update_time__range', update_time)
    print("QUERY: ", query)

    layanan_data = Layanan.annotate(key=F("id")).filter(**query).all()
    print("layanan_data: ", layanan_data)
    # Total
    total = await layanan_data.count()
    print("Total: ", total)
    # Query
    data = await layanan_data.limit(pageSize).offset(pageSize * (current - 1)).order_by("-create_time") \
        .values(
        "key", "id", "nomor_tiket", "jenis_layanan", "co_location", "perangkat", "mulai_kunjungan", "akhir_kunjungan","status","detail_tolak",
        "create_time", "update_time",)
    # print("DATA:", data)

    for item in data:
        if item["co_location"]:
            item["co_location"] = os.path.join("static", "upload", "file", item["co_location"])
    
    return res_antd(code=True, data=data, total=total)


@router.get("/upload/file/{file_name}")
async def get_file(file_name: str):
    # Konstruksi jalur lengkap menuju file gambar
    file_path = os.path.join("static", "upload", "file", file_name)

    # Periksa apakah file gambar ada atau tidak
    if not os.path.exists(file_path):
        # File tidak ditemukan, kembalikan tanggapan kesalahan atau foto default jika ada
        default_file_path = os.path.join("static", "upload", "file", "default.pdf")
        return FileResponse(default_file_path)

    # Kirimkan file gambar ke klien
    return FileResponse(file_path)


@router.get("/tiket", summary="Data Tiket")
async def tiket():
    data_tiket = await Layanan.all().values('nomor_tiket')

    if data_tiket:
        new_dict = {}
        for item in data_tiket:
            id = item['nomor_tiket']
            new_dict[id] = (item['nomor_tiket'])

        result = new_dict.items()
        return success(data=result)
    else:
        return fail(msg="Nomor Tiket Not Found!")


@router.get("/pengunjung", summary="Data Tiket")
async def pengunjung():
    data_pengunjung = await Layanan.all().values('pemandu')

    if data_pengunjung:
        new_dict = {}
        for item in data_pengunjung:
            id = item['pemandu']
            new_dict[id] = (item['pemandu'])

        result = new_dict.items()
        return success(data=result)
    else:
        return fail(msg="Nomor Tiket Not Found!")
    
@router.put("/tolak", summary="Tolak Layanan"
            # dependencies=[Security(check_permissions, scopes=["layanan_update"])]
            )
async def layanan_tolak(post: layanan.TolakLayanan):
    """
    Update layanan information
    :return:
    :param post:
    """
    layanan_check = await Layanan.get_or_none(pk=post.id)
    if not layanan_check:
        return fail(msg="Layanan does not exist")

    await Layanan.filter(pk=post.id).update(status=3, detail_tolak=post.detail_tolak)
    return success(msg="Updated!")