# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: BukuTamu
"""
import os
import time

from api.endpoints.common import write_access_log
from api.extends.sms import check_code
from core.Response import success, fail, res_antd
from models.buku_tamu import BukuTamu
from schemas import buku_tamu
from core.Utils import en_password, check_password, random_str
from core.Auth import create_access_token, check_permissions
from fastapi import Request, Query, APIRouter, Security, File, UploadFile
from config import settings
from typing import List
from tortoise.queryset import F


router = APIRouter(prefix='/buku_tamu')


@router.post("",
             summary="BukuTamu Add",
            #  dependencies=[Security(check_permissions, scopes=["buku_tamu_add"])]
             )
async def buku_tamu_add(post: buku_tamu.CreateBukuTamu):
    """
    BukuTamu Add
    :param post: CreateBukuTamu
    :return:
    """
    # Filter BukuTamus
    get_buku_tamu_no_tiket = await BukuTamu.get_or_none(no_tiket=post.no_tiket)

    if get_buku_tamu_no_tiket:
        return fail(msg=f"BukuTamu no_tiket {post.no_tiket} is exist!")

    # post.password = en_password(post.password)

    # Add User
    create_buku_tamu = await BukuTamu.create(**post.dict())
    if not create_buku_tamu:
        return fail(msg=f"Failed to create BukuTamu {post.no_tiket}!")
    return success(msg=f"Buku Tamu {create_buku_tamu.no_tiket} created successfully")


@router.delete(
        "",
        summary="BukuTamu Delete", 
        # dependencies=[Security(check_permissions, scopes=["buku_tamu_delete"])]
        )
async def buku_tamu_del(req: Request, id: int):
    """
    BukuTamu Delete
    :param req:
    :return:
    """
    delete_action = await BukuTamu.filter(pk=id).delete()
    if not delete_action:
        return fail(msg=f"failed to delete {id}!")
    return success(msg="successfully deleted")


@router.put("",
            summary="Update BukuTamu",
            # dependencies=[Security(check_permissions, scopes=["buku_tamu_update"])]
            )
async def buku_tamu_update(post: buku_tamu.UpdateBukuTamu):
    """
    Update buku_tamu information
    :param post:
    :return:
    """
    buku_tamu_check = await BukuTamu.get_or_none(pk=post.id)
    if not buku_tamu_check:
        return fail(msg="BukuTamu does not exist")
    if buku_tamu_check.no_tiket != post.no_tiket:
        check = await BukuTamu.get_or_none(no_tiket=post.no_tiket)
        if check:
            return fail(msg=f"BukuTamu no_tiket {check.no_tiket} exist!")

    data = post.dict()
    data.pop("id")
    await BukuTamu.filter(pk=post.id).update(**data)
    return success(msg="Updated!")


@router.get("",
            summary="BukuTamu List",
            response_model=buku_tamu.BukuTamuListData,
            # dependencies=[Security(check_permissions, scopes=["buku_tamu_query"])]
            )
async def buku_tamu_list(
        pageSize: int = 10,
        current: int = 1,
        no_tiket: str = Query(None),
        jam_masuk: str = Query(None),
        jam_keluar: str = Query(None),
        laporan_pekerjaan: str = Query(None),
        daftar_pengunjung: str = Query(None),
        create_time: str = Query(None),
        update_time: str = Query(None),

):
    """
    Get All BukuTamus
    :return:
    """
    # Query Conditions
    query = {}
    if no_tiket:
        query.setdefault('no_tiket__icontains', no_tiket)
    if jam_masuk:
        query.setdefault('jam_masuk', jam_masuk)
    if jam_keluar:
        query.setdefault('jam_keluar', jam_keluar)
    if laporan_pekerjaan:
        query.setdefault('laporan_pekerjaan', laporan_pekerjaan)
    if daftar_pengunjung:
        query.setdefault('daftar_pengunjung', daftar_pengunjung)
    if create_time:
        query.setdefault('create_time__range', create_time)
    if update_time:
        query.setdefault('update_time__range', update_time)
        

    buku_tamu_data = BukuTamu.annotate(key=F("id")).filter(**query).all()
    # Total
    total = await buku_tamu_data.count()
    # Query
    data = await buku_tamu_data.limit(pageSize).offset(pageSize * (current - 1)).order_by("-create_time") \
        .values(
        "key", "id", "no_tiket", "jam_masuk", "jam_keluar", "laporan_pekerjaan", "daftar_pengunjung", "create_time", "update_time")

    return res_antd(code=True, data=data, total=total)
