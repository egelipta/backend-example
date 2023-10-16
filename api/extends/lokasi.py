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
from models.lokasi import Lokasi
from schemas import lokasi
from core.Utils import en_password, check_password, random_str
from core.Auth import create_access_token, check_permissions
from fastapi import Request, Query, APIRouter, Security, File, UploadFile
from config import settings
from typing import List
from tortoise.queryset import F


router = APIRouter(prefix='/lokasi')


@router.post("",
             summary="Lokasi Add",
            #  dependencies=[Security(check_permissions, scopes=["lokasi_add"])]
             )
async def lokasi_add(post: lokasi.CreateLokasi):
    """
    Lokasi Add
    :param post: CreateLokasi
    :return:
    """
    # Filter Lokasis
    get_lokasi = await Lokasi.get_or_none(merek=post.merek, tipe=post.tipe)

    if get_lokasi:
        return fail(msg=f"Lokasi merek {post.merek} is exist!")

    # post.password = en_password(post.password)

    # Add User
    create_lokasi = await Lokasi.create(**post.dict())
    if not create_lokasi:
        return fail(msg=f"Failed to create Lokasi {post.merek}!")
    return success(msg=f"Merek dan Tipe {create_lokasi.merek} created successfully")


@router.delete(
        "",
        summary="Lokasi Delete", 
        # dependencies=[Security(check_permissions, scopes=["lokasi_delete"])]
        )
async def lokasi_del(req: Request, id: int):
    """
    Lokasi Delete
    :param req:
    :return:
    """
    delete_action = await Lokasi.filter(pk=id).delete()
    if not delete_action:
        return fail(msg=f"failed to delete {id}!")
    return success(msg="successfully deleted")


@router.put("",
            summary="Update Lokasi",
            # dependencies=[Security(check_permissions, scopes=["lokasi_update"])]
            )
async def lokasi_update(post: lokasi.UpdateLokasi):
    """
    Update lokasi information
    :param post:
    :return:
    """
    lokasi_check = await Lokasi.get_or_none(pk=post.id)
    if not lokasi_check:
        return fail(msg="Lokasi does not exist")
    if lokasi_check.merek != post.merek:
        check = await Lokasi.get_or_none(merek=post.merek)
        if check:
            return fail(msg=f"Lokasi merek {check.merek} exist!")

    data = post.dict()
    data.pop("id")
    await Lokasi.filter(pk=post.id).update(**data)
    return success(msg="Updated!")


@router.get("",
            summary="Lokasi List",
            response_model=lokasi.LokasiListData,
            # dependencies=[Security(check_permissions, scopes=["lokasi_query"])]
            )
async def lokasi_list(
        pageSize: int = 10,
        current: int = 1,
        merek: str = Query(None),
        tipe: str = Query(None),
        create_time: str = Query(None),
        update_time: str = Query(None),

):
    """
    Get All Lokasis
    :return:
    """
    # Query Conditions
    query = {}
    if merek:
        query.setdefault('merek__icontains', merek)
    if tipe:
        query.setdefault('tipe', tipe)
    if create_time:
        query.setdefault('create_time__range', create_time)
    if update_time:
        query.setdefault('update_time__range', update_time)
        

    lokasi_data = Lokasi.annotate(key=F("id")).filter(**query).all()
    # Total
    total = await lokasi_data.count()
    # Query
    data = await lokasi_data.limit(pageSize).offset(pageSize * (current - 1)).order_by("-create_time") \
        .values(
        "key", "id", "merek", "tipe", "create_time", "update_time")

    return res_antd(code=True, data=data, total=total)



@router.get("/lokasi", summary="Get data lokasi")
async def dataLokasi():
    data_lokasi = await Lokasi.all().distinct().values_list('lokasi', flat=True)
    print(data_lokasi)

    
    if data_lokasi:
        # new_array = []
        # for item in data_merek:
        #     new_array.append(item.tipe)

        # result = new_array
        return success(data=data_lokasi)
    else:
        return fail(msg="Lokasi not found!")
    

@router.get("/nama_ruangan", summary="Get data nama_ruangan")
async def nama_ruangan(lokasi: str):
    # merek = Request.param.merek
    print("lokasi: ",lokasi)
    nama_ruangan = await Lokasi.filter(lokasi=lokasi)
    # tipe = tipe.filter()

    if nama_ruangan:
        new_array = []
        for item in nama_ruangan:
            new_array.append(item.nama_ruangan)

        result = set(new_array)
        return success(data=result)
    else:
        return fail(msg="Nama Ruangan Not Found!")
    
@router.get("/rak", summary="Get data rak")
async def rak(lokasi: str, nama_ruangan: str):
    # merek = Request.param.merek
    print("nama_ruangan: ",nama_ruangan)
    rak = await Lokasi.filter(lokasi=lokasi, nama_ruangan=nama_ruangan)
    # tipe = tipe.filter()

    if rak:
        new_array = []
        for item in rak:
            new_array.append(item.posisi_rak)

        result = set(new_array)
        return success(data=result)
    else:
        return fail(msg="Nama Ruangan Not Found!")
    
@router.get("/posisi_u", summary="Get data rak")
async def posisi_u_data(lokasi: str, nama_ruangan: str, posisi_rak: str):
    # merek = Request.param.merek
    print("rak: ",posisi_rak)
    posisi_u = await Lokasi.filter(lokasi=lokasi, nama_ruangan=nama_ruangan, posisi_rak=posisi_rak, sn_aset='kosong')
    # tipe = tipe.filter()

    if posisi_u:
        new_array = []
        for item in posisi_u:
            new_array.append(item.posisi_u)

        result = new_array
        return success(data=result)
    else:
        return fail(msg="Nama Ruangan Not Found!")


