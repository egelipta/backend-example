# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: Pemandu Management
"""
import os
import time

from api.endpoints.common import write_access_log
from api.extends.sms import check_code
from core.Response import success, fail, res_antd
from models.pemandu import Pemandu
from schemas import pemandu
from core.Utils import en_password, check_password, random_str
from core.Auth import create_access_token, check_permissions
from fastapi import Request, Query, APIRouter, Security, File, UploadFile
from config import settings
from typing import List
from tortoise.queryset import F


router = APIRouter(prefix='/pemandu')


@router.post("", summary="Pemandu Add")
async def pemandu_add(post: pemandu.CreatePemandu):
    """
    Pemandu Add
    :param post: CreatePemandu
    :return:
    """
    # Filter Pemandus
    get_pemandu_nama = await Pemandu.get_or_none(nama=post.nama)

    if get_pemandu_nama:
        return fail(msg=f"Pemandu nama {post.nama} is exist!")

    # Add Pemandu
    create_pemandu = await Pemandu.create(**post.dict())
    if not create_pemandu:
        return fail(msg=f"Failed to create Pemandu {post.nama}!")
    return success(msg=f"Pemandu {create_pemandu.nama} created successfully")


@router.delete("", summary="Pemandu Delete")
async def pemandu_del(req: Request, id: int):
    """
    Pemandu Delete
    :param req:
    :return:
    """
    pemandu = await Pemandu.get_or_none(pk=id)
    if not pemandu:
        return fail(msg="ID does not exist!")
    result = await Pemandu.filter(pk=id).delete()
    if not result:
        return fail(msg="failed to delete!")
    return success(msg="successfully deleted!")


@router.put("", summary="Update Pemandu")
async def pemandu_update(post: pemandu.UpdatePemandu):
    """
    Update pemandu information
    :return:
    :param post:
    """
    pemandu_check = await Pemandu.get_or_none(pk=post.id)
    if not pemandu_check:
        return fail(msg="Pemandu does not exist")
    if pemandu_check.nama != post.nama:
        check = await Pemandu.get_or_none(nama=post.nama)
        if check:
            return fail(msg=f"Pemandu nama {check.nama} exist!")
    if pemandu_check.no_hp != post.no_hp:
        check = await Pemandu.get_or_none(no_hp=post.no_hp)
        if check:
            return fail(msg=f"Pemandu no_hp {check.no_hp} exist!")
    
    # if pemandu_check.access_type != post.access_type:
    #     check = await Pemandu.get_or_none(access_type=post.access_type)
    #     if check:
    #         return fail(msg=f"Pemandu access_type {check.access_type} exist!")
    # if pemandu_check.status != post.status:
    #     check = await Pemandu.get_or_none(status=post.status)
    #     if check:
    #         return fail(msg=f"Pemandu status {check.status} exist!")
    # if pemandu_check.group != post.group:
    #     check = await Pemandu.get_or_none(group=post.group)
    #     if check:
    #         return fail(msg=f"Pemandu group {check.group} exist!")
    # if pemandu_check.expire_time != post.expire_time:
    #     check = await Pemandu.get_or_none(expire_time=post.expire_time)
    #     if check:
    #         return fail(msg=f"Pemandu expire_time {check.expire_time} exist!")
    # if pemandu_check.gender != post.gender:
    #     check = await Pemandu.get_or_none(gender=post.gender)
    #     if check:
    #         return fail(msg=f"Pemandu gender {check.gender} exist!")
    # if pemandu_check.birthday != post.birthday:
    #     check = await Pemandu.get_or_none(birthday=post.birthday)
    #     if check:
    #         return fail(msg=f"Pemandu birthday {check.birthday} exist!")
    # if pemandu_check.second_contact != post.second_contact:
    #     check = await Pemandu.get_or_none(second_contact=post.second_contact)
    #     if check:
    #         return fail(msg=f"Pemandu second_contact {check.second_contact} exist!")
    # if pemandu_check.blacklist != post.blacklist:
    #     check = await Pemandu.get_or_none(blacklist=post.blacklist)
    #     if check:
    #         return fail(msg=f"Pemandu blacklist {check.blacklist} exist!")

    data = post.dict()
    data.pop("id")
    await Pemandu.filter(pk=post.id).update(**data)
    return success(msg="Updated!")


@router.get("",
            summary="Pemandu List",
            response_model=pemandu.PemanduListData
            )
async def pemandu_list(
        pageSize: int = 10,
        current: int = 1,
        nama: str = Query(None),
        no_hp: str = Query(None),
        create_time: str = Query(None),
        update_time: str = Query(None),
):
    """
    Get All Pemandus
    :return:
    """
    # Query Conditions
    query = {}
    if nama:
        query.setdefault('nama__icontains', nama)
    if no_hp:
        query.setdefault('no_hp__icontains', no_hp)
    if create_time:
        query.setdefault('create_time__range', create_time)
    if update_time:
        query.setdefault('update_time__range', update_time)

    pemandu_data = Pemandu.annotate(key=F("id")).filter(**query).all()
    # Total
    total = await pemandu_data.count()
    # Query
    data = await pemandu_data.limit(pageSize).offset(pageSize * (current - 1)).order_by("-create_time") \
        .values(
        "key",
        "id",
        "nama",
        "no_hp",
        "create_time",
        "update_time",)

    return res_antd(code=True, data=data, total=total)

@router.get("/dataPemandu", summary="Data Pemandu")
async def dataPemandu(req: Request):
    data_perangkat = await Pemandu.all().values('nama','no_hp')

    if data_perangkat:
        new_dict = {}
        for item in data_perangkat:
            id = f"{item['nama']} - {item['no_hp']} "
            new_dict[id] = f"{item['nama']} - {item['no_hp']} "

        result = new_dict.items()
        return success(data=result)
    else:
        return fail(msg="Data Perangkat Not Found!")
