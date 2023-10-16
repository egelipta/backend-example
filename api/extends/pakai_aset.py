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
from models.pakai_aset import PakaiAset
from schemas import pakai_aset
from models.aset import Aset
from schemas import aset
from core.Utils import en_password, check_password, random_str
from core.Auth import create_access_token, check_permissions
from fastapi import Request, Query, APIRouter, Security, File, UploadFile
from config import settings
from typing import List
from tortoise.queryset import F


router = APIRouter(prefix='/pakai_Aset')


@router.post("",
             summary="PakaiAset Add",
            #  dependencies=[Security(check_permissions, scopes=["pengunjung_hadir_add"])]
             )
async def pakai_aset_add(post: pakai_aset.InsertAkanPakaiAset):
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
    ns = post.nomor_seri
    print(len(ns))
   
    for x in range(len(ns)):
        await PakaiAset.create(nomor_seri=ns[x], nomor_tiket=no_tikets)
            

    return success(msg=f"Sukses")

@router.get("/layanan_perangkat", summary="Data Perangkat")
async def layanan_perangkat(
        pageSize: int = 10,
        current: int = 1,
        id: int = Query(None),
        nomor_seri: str = Query(None),
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
    if nomor_seri:
        query.setdefault('nomor_seri', nomor_seri)
    if nomor_tiket:
        query.setdefault('nomor_tiket', nomor_tiket)

    
   
    device_names = []
    # record_data = record_access.all()
    # Total
    total = await PakaiAset.filter(**query).count()
    data = await PakaiAset.filter(**query).all()
    # device_names = await Device.filter(id=data.id_device)

    # devices = await Device.all()
   
    
    for i in data :
        device_name = await Aset.annotate(key=F("id")).filter(nomor_seri = i.nomor_seri).values("key",
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
        "update_time")
        device_names.append(device_name[0])

    return res_antd(code=True, data=device_names, total=len(device_names))