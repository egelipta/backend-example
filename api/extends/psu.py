# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: Psu
"""
import os
import time

from api.endpoints.common import write_access_log
from api.extends.sms import check_code
from core.Response import success, fail, res_antd
from models.psu import Psu
from schemas import psu
from core.Utils import en_password, check_password, random_str
from core.Auth import create_access_token, check_permissions
from fastapi import Request, Query, APIRouter, Security, File, UploadFile
from config import settings
from typing import List
from tortoise.queryset import F


router = APIRouter(prefix='/psu')


@router.post("",
             summary="Psu Add",
            #  dependencies=[Security(check_permissions, scopes=["psu_add"])]
             )
async def psu_add(post: psu.CreatePsu):
    """
    Psu Add
    :param post: CreatePsu
    :return:
    """
    # Filter Psus
    # get_psu_name = await Psu.get_or_none(name=post.name)

    # if get_psu_name:
    #     return fail(msg=f"Psu name {post.name} is exist!")

    # post.password = en_password(post.password)

    # Add User
    create_psu = await Psu.create(**post.dict())
    if not create_psu:
        return fail(msg=f"Failed to create Psu !")
    return success(msg=f"PSU berhasil ditambahkan")


@router.delete(
        "",
        summary="Psu Delete", 
        # dependencies=[Security(check_permissions, scopes=["psu_delete"])]
        )
async def psu_del(req: Request, id: int):
    """
    Psu Delete
    :param req:
    :return:
    """
    delete_action = await Psu.filter(pk=id).delete()
    if not delete_action:
        return fail(msg=f"failed to delete {id}!")
    return success(msg="successfully deleted")


@router.put("",
            summary="Update Psu",
            # dependencies=[Security(check_permissions, scopes=["psu_update"])]
            )
async def psu_update(post: psu.UpdatePsu):
    """
    Update psu information
    :param post:
    :return:
    """
    # psu_check = await Psu.get_or_none(pk=post.id)
    # if not psu_check:
    #     return fail(msg="Psu does not exist")
    # if psu_check.name != post.name:
    #     check = await Psu.get_or_none(name=post.name)
    #     if check:
    #         return fail(msg=f"Psu name {check.name} exist!")

    data = post.dict()
    data.pop("id")
    await Psu.filter(pk=post.id).update(**data)
    return success(msg="Updated!")


@router.get("",
            summary="Psu List",
            response_model=psu.PsuListData,
            # dependencies=[Security(check_permissions, scopes=["psu_query"])]
            )
async def psu_list(
        pageSize: int = 10,
        current: int = 1,
        power: str = Query(None),
        tipe_socket: str = Query(None),
        id_aset: str = Query(None),
        create_time: str = Query(None),
        update_time: str = Query(None),


):
    """
    Get All Psus
    :return:
    """
    # Query Conditions
    query = {}
    if power:
        query.setdefault('name__icontains', power)
    if tipe_socket:
        query.setdefault('seri_merk', tipe_socket)
    if id_aset:
        query.setdefault('seri_merk', id_aset)
    if create_time:
        query.setdefault('create_time__range', create_time)
    if update_time:
        query.setdefault('update_time__range', update_time)
        

    psu_data = Psu.annotate(key=F("id")).filter(**query).all()
    # Total
    total = await psu_data.count()
    # Query
    data = await psu_data.limit(pageSize).offset(pageSize * (current - 1)).order_by("-create_time") \
        .values(
        "key", "id", "power", "tipe_socket","id_aset", "create_time", "update_time")
    

    return res_antd(code=True, data=data, total=total)



@router.get("/dataPsu", summary="Get data psu")
async def dataPsu():
    data_psu = await Psu(family=1).all().values('name')

    if data_psu:
        new_dict = {}
        for item in data_psu:
            id = item['name']
            new_dict[id] = (item['name'])

        result = new_dict.items()
        return success(data=result)
    else:
        return fail(msg="Psu Not Found!")
    

@router.get("/seri", summary="Get data seri")
async def seri():
    seri = await Psu(family=1).all().values('seri_merk')

    if seri:
        new_dict = {}
        for item in seri:
            id = item['seri_merk']
            new_dict[id] = (item['seri_merk'])

        result = new_dict.items()
        return success(data=result)
    else:
        return fail(msg="Seri Not Found!")
