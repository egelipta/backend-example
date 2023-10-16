# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: MerekTipe
"""
import os
import time

from api.endpoints.common import write_access_log
from api.extends.sms import check_code
from core.Response import success, fail, res_antd
from models.merek_tipe import MerekTipe
from schemas import merek_tipe
from core.Utils import en_password, check_password, random_str
from core.Auth import create_access_token, check_permissions
from fastapi import Request, Query, APIRouter, Security, File, UploadFile
from config import settings
from typing import List
from tortoise.queryset import F


router = APIRouter(prefix='/merek_tipe')


@router.post("",
             summary="MerekTipe Add",
            #  dependencies=[Security(check_permissions, scopes=["merek_tipe_add"])]
             )
async def merek_tipe_add(post: merek_tipe.CreateMerekTipe):
    """
    MerekTipe Add
    :param post: CreateMerekTipe
    :return:
    """
    # Filter MerekTipes
    get_merek_tipe = await MerekTipe.get_or_none(merek=post.merek, tipe=post.tipe)

    if get_merek_tipe:
        return fail(msg=f"MerekTipe merek {post.merek} is exist!")

    # post.password = en_password(post.password)

    # Add User
    create_merek_tipe = await MerekTipe.create(**post.dict())
    if not create_merek_tipe:
        return fail(msg=f"Failed to create MerekTipe {post.merek}!")
    return success(msg=f"Merek dan Tipe {create_merek_tipe.merek} created successfully")


@router.delete(
        "",
        summary="MerekTipe Delete", 
        # dependencies=[Security(check_permissions, scopes=["merek_tipe_delete"])]
        )
async def merek_tipe_del(req: Request, id: int):
    """
    MerekTipe Delete
    :param req:
    :return:
    """
    delete_action = await MerekTipe.filter(pk=id).delete()
    if not delete_action:
        return fail(msg=f"failed to delete {id}!")
    return success(msg="successfully deleted")


@router.put("",
            summary="Update MerekTipe",
            # dependencies=[Security(check_permissions, scopes=["merek_tipe_update"])]
            )
async def merek_tipe_update(post: merek_tipe.UpdateMerekTipe):
    """
    Update merek_tipe information
    :param post:
    :return:
    """
    merek_tipe_check = await MerekTipe.get_or_none(pk=post.id)
    if not merek_tipe_check:
        return fail(msg="MerekTipe does not exist")
    if merek_tipe_check.merek != post.merek:
        check = await MerekTipe.get_or_none(merek=post.merek)
        if check:
            return fail(msg=f"MerekTipe merek {check.merek} exist!")

    data = post.dict()
    data.pop("id")
    await MerekTipe.filter(pk=post.id).update(**data)
    return success(msg="Updated!")


@router.get("",
            summary="MerekTipe List",
            response_model=merek_tipe.MerekTipeListData,
            # dependencies=[Security(check_permissions, scopes=["merek_tipe_query"])]
            )
async def merek_tipe_list(
        pageSize: int = 10,
        current: int = 1,
        merek: str = Query(None),
        tipe: str = Query(None),
        create_time: str = Query(None),
        update_time: str = Query(None),

):
    """
    Get All MerekTipes
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
        

    merek_tipe_data = MerekTipe.annotate(key=F("id")).filter(**query).all()
    # Total
    total = await merek_tipe_data.count()
    # Query
    data = await merek_tipe_data.limit(pageSize).offset(pageSize * (current - 1)).order_by("-create_time") \
        .values(
        "key", "id", "merek", "tipe", "create_time", "update_time")

    return res_antd(code=True, data=data, total=total)



@router.get("/merek", summary="Get data merek")
async def dataMerek():
    data_merek = await MerekTipe.all().distinct().values_list('merek', flat=True)
    print(data_merek)

    
    if data_merek:
        # new_array = []
        # for item in data_merek:
        #     new_array.append(item.tipe)

        # result = new_array
        return success(data=data_merek)
    else:
        return fail(msg="Merek not found!")
    

@router.get("/tipe", summary="Get data tipe")
async def tipe(merek: str):
    # merek = Request.param.merek
    print("merek: ",merek)
    tipe = await MerekTipe.filter(merek=merek)
    # tipe = tipe.filter()

    if tipe:
        new_array = []
        for item in tipe:
            new_array.append(item.tipe)

        result = new_array
        return success(data=result)
    else:
        return fail(msg="Seri Not Found!")


