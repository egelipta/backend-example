# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: Lokasi
"""
import os
import time

from api.endpoints.common import write_access_log
from api.extends.sms import check_code
from core.Response import success, fail, res_antd
from models.power import Power
from schemas.power import InsertPower, PowerListData, PowerDelete, PutPower
from core.Utils import en_password, check_password, random_str
from core.Auth import create_access_token, check_permissions
from fastapi import Request, Query, APIRouter, Security, File, UploadFile
from config import settings
from typing import List
from tortoise.queryset import F


router = APIRouter(prefix='/power')

@router.post("", summary="Power Add")
async def power_add(post: InsertPower):
    """
    Pemandu Add
    :param post: CreatePemandu
    :return:
    """
    # # Filter Pemandus
    # get_pemandu_nama = await Power.get_or_none(lokasi=post.lokasi, 
    #                                            nama_ruangan=post.nama_ruangan, 
    #                                            posisi_rak=post.posisi_rak
    #                                            )

    # get_power_nama = await Power.get_or_none(nama=post.nama)

    # if not get_pemandu_nama:
    #     return fail(msg=f"Anda belum memilih lokasi!")
    
    # if get_power_nama:
    #     return fail(msg=f"PDU {post.nama} sudah ada!")
    
    
    i=0
    xy=1
    for x in post.tipe:
            for y in range(post.jumlah[i]):
                await Power.create(lokasi=post.lokasi, nama_ruangan=post.nama_ruangan, posisi_rak=post.posisi_rak, nama=post.nama, source=post.source, power=xy,tipe=post.tipe[i], sn_aset='kosong')
                xy+=1
            i+=1
            

    return success(msg=f"Power created successfully")

@router.put("", summary="Power Put")
async def power_put(post: PutPower):
    """
    Pemandu Add
    :param post: CreatePemandu
    :return:
    """
    # # Filter Pemandus
    # get_pemandu_nama = await Power.get_or_none(lokasi=post.lokasi, 
    #                                            nama_ruangan=post.nama_ruangan, 
    #                                            posisi_rak=post.posisi_rak
    #                                            )

    # get_power_nama = await Power.get_or_none(nama=post.nama)

    # if not get_pemandu_nama:
    #     return fail(msg=f"Anda belum memilih lokasi!")
    
    # if get_power_nama:
    #     return fail(msg=f"PDU {post.nama} sudah ada!")
    
    
    i=0
    xy=1
    for x in post.id:
            await Power.filter(id=post.id[i]).update(sn_aset=post.sn_aset)
            i+=1
            

    return success(msg=f"Put Power successfully")

@router.delete("", summary="Power Delete")
async def power_del(req: Request, id: int):
    """
    Pemandu Delete
    :param req:
    :return:
    """
    pemandu = await Power.get_or_none(pk=id, sn_aset='' )
    if not pemandu:
        return fail(msg="Sedang dipakai!")
    result = await Power.filter(pk=id).delete()
    if not result:
        return fail(msg="failed to delete!")
    return success(msg="successfully deleted!")

@router.get("",
            summary="Power List",
            response_model=PowerListData
            )
async def power_list(
        pageSize: int = 10,
        current: int = 1,
        lokasi: str = Query(None),
        nama_ruangan: str = Query(None),
        sn_aset: str = Query(None),
        posisi_rak: str = Query(None),
        create_time: str = Query(None),
        update_time: str = Query(None),

):
    """
    Get All Pemandus
    :return:
    """
    # Query Conditions
    query = {}
    if lokasi:
        query.setdefault('lokasi__icontains', lokasi)
    if nama_ruangan:
        query.setdefault('nama_ruangan__icontains', nama_ruangan)
    if posisi_rak:
        query.setdefault('posisi_rak__icontains', posisi_rak)
    if sn_aset:
        query.setdefault('sn_aset', sn_aset)
    if create_time:
        query.setdefault('create_time__range', create_time)
    if update_time:
        query.setdefault('update_time__range', update_time)

    power_data = Power.annotate(key=F("id")).filter(**query).all()
    # Total
    total = await power_data.count()
    # Query
    data = await power_data.limit(pageSize).offset(pageSize * (current - 1)).order_by("-create_time") \
        .values(
        "key",
        "id",
        "nama",
        "lokasi",
        "nama_ruangan",
        "posisi_rak",
        "power",
        "source",
        "tipe",
        "sn_aset",
        "create_time",
        "update_time",)

    return res_antd(code=True, data=data, total=total)


@router.delete("", summary="Pemandu Delete")
async def power_del(req: Request, id: int):
    """
    Pemandu Delete
    :param req:
    :return:
    """
    pemandu = await Power.get_or_none(pk=id)
    if not pemandu:
        return fail(msg="ID does not exist!")
    result = await Power.filter(pk=id).delete()
    if not result:
        return fail(msg="failed to delete!")
    return success(msg="successfully deleted!")

    
@router.get("/power_a", summary="Get data power A")
async def power_a_data(lokasi: str, nama_ruangan: str, posisi_rak: str):
    # merek = Request.param.merek
    print("rak: ",posisi_rak)
    power_a = await Power.filter(lokasi=lokasi, nama_ruangan=nama_ruangan, posisi_rak=posisi_rak, source='A', sn_aset='kosong')
    # source = source.filter()

    if power_a:
        new_array = []
        for item in power_a:
            new_array.append(item.power)

        result = new_array
        return success(data=result)
    else:
        return fail(msg="Nama Ruangan Not Found!")
    

   
@router.get("/power_b", summary="Get data power B")
async def power_a_data(lokasi: str, nama_ruangan: str, posisi_rak: str):
    # merek = Request.param.merek
    print("rak: ",posisi_rak)
    power_a = await Power.filter(lokasi=lokasi, nama_ruangan=nama_ruangan, posisi_rak=posisi_rak, source='B', sn_aset='')
    # source = source.filter()

    if power_a:
        new_array = []
        for item in power_a:
            new_array.append(item.power)

        result = new_array
        return success(data=result)
    else:
        return fail(msg="Nama Ruangan Not Found!")


