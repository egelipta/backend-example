# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: PengunjungHadir
"""
import os
import time

from api.endpoints.common import write_access_log
from api.extends.sms import check_code
from core.Response import success, fail, res_antd
from models.pengunjung_hadir import PengunjungHadir
from schemas import pengunjung_hadir
from models.daftar_pengunjung import DaftarPengunjung
from schemas import daftar_pengunjung
from core.Utils import en_password, check_password, random_str
from core.Auth import create_access_token, check_permissions
from fastapi import Request, Query, APIRouter, Security, File, UploadFile
from config import settings
from typing import List
from tortoise.queryset import F


router = APIRouter(prefix='/pengunjung_hadir')


@router.post("",
             summary="PengunjungHadir Add",
            #  dependencies=[Security(check_permissions, scopes=["pengunjung_hadir_add"])]
             )
async def pengunjung_hadir_add(post: pengunjung_hadir.InsertAkanHadir):
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
    no_tikets = post.nomor_tiket
    niks = post.nik
    print(len(niks))
   
    for x in range(len(niks)):
        await PengunjungHadir.create(nik=niks[x], nomor_tiket=no_tikets)
            

    return success(msg=f"Sukses")


@router.delete(
        "",
        summary="PengunjungHadir Delete", 
        # dependencies=[Security(check_permissions, scopes=["pengunjung_hadir_delete"])]
        )
async def pengunjung_hadir_del(req: Request, id: int):
    """
    PengunjungHadir Delete
    :param req:
    :return:
    """
    delete_action = await PengunjungHadir.filter(pk=id).delete()
    if not delete_action:
        return fail(msg=f"failed to delete {id}!")
    return success(msg="successfully deleted")


@router.get("/layanan_pengunjung", summary="Data Pengunjung")
async def layanan_perangkat(
        pageSize: int = 10,
        current: int = 1,
        id: int = Query(None),
        nik: str = Query(None),
        nomor_tiket: str = Query(None),
        
):
    """
    Get All Employees
    :return:
    """
    # Query Conditions
    query = {}
    if id:
        query.setdefault('id', id)
    if nik:
        query.setdefault('nik', nik)
    if nomor_tiket:
        query.setdefault('nomor_tiket', nomor_tiket)

    
   
    device_names = []
    # record_data = record_access.all()
    # Total
    total = await PengunjungHadir.filter(**query).count()
    data = await PengunjungHadir.filter(**query).all()
    # device_names = await Device.filter(id=data.id_device)

    # devices = await Device.all()
   
    
    for i in data :
        device_name = await DaftarPengunjung.annotate(key=F("id")).filter(nik = i.nik).values(
        "key", "id", "nama", "nik", "status", "instansi", "foto", "create_time", "update_time")
        device_names.append(device_name[0])

    return res_antd(code=True, data=device_names, total=len(device_names))