# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: DaftarPengunjung Management
"""
import os
import time

from api.endpoints.common import write_access_log
from api.extends.sms import check_code
from core.Response import success, fail, res_antd
from models.daftar_pengunjung import DaftarPengunjung
from schemas import daftar_pengunjung
from core.Utils import en_password, check_password, random_str
from core.Auth import create_access_token, check_permissions
from fastapi import Request, Query, APIRouter, Security, File, UploadFile
from config import settings
from typing import List
from tortoise.queryset import F

import os
from fastapi.responses import FileResponse
from models.daftar_pengunjung import DaftarPengunjung


router = APIRouter(prefix='/daftar_pengunjung')


@router.post("",
             summary="DaftarPengunjung Add",
            #  dependencies=[Security(check_permissions, scopes=["daftar_pengunjung_add"])]
             )
async def daftar_pengunjung_add(post: daftar_pengunjung.CreateDaftarPengunjung):
    """
    DaftarPengunjung Add
    :param post: CreateDaftarPengunjung
    :return:
    """
    # Filter DaftarPengunjungs
    get_daftar_pengunjung_nama = await DaftarPengunjung.get_or_none(nama=post.nama)

    if get_daftar_pengunjung_nama:
        return fail(msg=f"Daftar Pengunjung nama {post.nama} is exist!")

    # post.password = en_password(post.password)

    # Add User
    create_daftar_pengunjung = await DaftarPengunjung.create(**post.dict())
    if not create_daftar_pengunjung:
        return fail(msg=f"Failed to create DaftarPengunjung {post.nama}!")
    return success(msg=f"Daftar Pengunjung {create_daftar_pengunjung.nama} created successfully")


@router.delete(
        "",
        summary="DaftarPengunjung Delete", 
        # dependencies=[Security(check_permissions, scopes=["daftar_pengunjung_delete"])]
        )
async def daftar_pengunjung_del(req: Request, id: int):
    """
    DaftarPengunjung Delete
    :param req:
    :return:
    """
    delete_action = await DaftarPengunjung.filter(pk=id).delete()
    if not delete_action:
        return fail(msg=f"failed to delete {id}!")
    return success(msg="successfully deleted")


@router.put("",
            summary="Update DaftarPengunjung",
            # dependencies=[Security(check_permissions, scopes=["daftar_pengunjung_update"])]
            )
async def daftar_pengunjung_update(post: daftar_pengunjung.UpdateDaftarPengunjung):
    """
    Update daftar_pengunjung information
    :param post:
    :return:
    """
    daftar_pengunjung_check = await DaftarPengunjung.get_or_none(pk=post.id)
    if not daftar_pengunjung_check:
        return fail(msg="DaftarPengunjung does not exist")
    if daftar_pengunjung_check.nama != post.nama:
        check = await DaftarPengunjung.get_or_none(nama=post.nama)
        if check:
            return fail(msg=f"Daftar Pengunjung nama {check.nama} exist!")

    data = post.dict()
    data.pop("id")
    await DaftarPengunjung.filter(pk=post.id).update(**data)
    return success(msg="Updated!")


@router.get("",
            summary="DaftarPengunjung List",
            response_model=daftar_pengunjung.DaftarPengunjungListData,
            # dependencies=[Security(check_permissions, scopes=["daftar_pengunjung_query"])]
            )
async def daftar_pengunjung_list(
        pageSize: int = 10,
        current: int = 1,
        nama: str = Query(None),
        nik: str = Query(None),
        status: str = Query(None),
        instansi: str = Query(None),
        foto: str = Query(None),
        create_time: str = Query(None),
        update_time: str = Query(None),

):
    """
    Get All DaftarPengunjungs
    :return:
    """
    # Query Conditions
    query = {}
    if nama:
        query.setdefault('nama__icontains', nama)
    if nik:
        query.setdefault('nik', nik)
    if status:
        query.setdefault('status', status)
    if instansi:
        query.setdefault('instansi', instansi)
    if foto:
        query.setdefault('foto', foto)
    if create_time:
        query.setdefault('create_time__range', create_time)
    if update_time:
        query.setdefault('update_time__range', update_time)
        

    daftar_pengunjung_data = DaftarPengunjung.annotate(key=F("id")).filter(**query).all()
    # Total
    total = await daftar_pengunjung_data.count()
    # Query
    data = await daftar_pengunjung_data.limit(pageSize).offset(pageSize * (current - 1)).order_by("-create_time") \
        .values(
        "key", "id", "nama", "nik", "status", "instansi", "foto", "create_time", "update_time")

    print("DATA:", data)

    # Tambahkan jalur lengkap untuk setiap gambar yang akan ditampilkan
    for item in data:
        if item["foto"]:
            item["foto"] = os.path.join("static", "upload", "photo", item["foto"])

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


@router.get("/pengunjung", summary="Data Pengunjung")
async def pengunjung():
    data_pengunjung = await DaftarPengunjung.all().values('nama','nik')

    if data_pengunjung:
        new_dict = {}
        for item in data_pengunjung:
            id = item['nik']
            new_dict[id] =  f"{item['nik']} - {item['nama']}"
           

        result = new_dict.items()
        return success(data=result)
    else:
        return fail(msg="Data Pengunjung Not Found!")
