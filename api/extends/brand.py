# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: Brand
"""
import os
import time

from api.endpoints.common import write_access_log
from api.extends.sms import check_code
from core.Response import success, fail, res_antd
from models.brand import Brand
from schemas import brand
from core.Utils import en_password, check_password, random_str
from core.Auth import create_access_token, check_permissions
from fastapi import Request, Query, APIRouter, Security, File, UploadFile
from config import settings
from typing import List
from tortoise.queryset import F


router = APIRouter(prefix='/brand')


@router.post("",
             summary="Brand Add",
            #  dependencies=[Security(check_permissions, scopes=["brand_add"])]
             )
async def brand_add(post: brand.CreateBrand):
    """
    Brand Add
    :param post: CreateBrand
    :return:
    """
    # Filter Brands
    get_brand_name = await Brand.get_or_none(name=post.name)

    if get_brand_name:
        return fail(msg=f"Brand name {post.name} is exist!")

    # post.password = en_password(post.password)

    # Add User
    create_brand = await Brand.create(**post.dict())
    if not create_brand:
        return fail(msg=f"Failed to create Brand {post.name}!")
    return success(msg=f"Buku Tamu {create_brand.name} created successfully")


@router.delete(
        "",
        summary="Brand Delete", 
        # dependencies=[Security(check_permissions, scopes=["brand_delete"])]
        )
async def brand_del(req: Request, id: int):
    """
    Brand Delete
    :param req:
    :return:
    """
    delete_action = await Brand.filter(pk=id).delete()
    if not delete_action:
        return fail(msg=f"failed to delete {id}!")
    return success(msg="successfully deleted")


@router.put("",
            summary="Update Brand",
            # dependencies=[Security(check_permissions, scopes=["brand_update"])]
            )
async def brand_update(post: brand.UpdateBrand):
    """
    Update brand information
    :param post:
    :return:
    """
    brand_check = await Brand.get_or_none(pk=post.id)
    if not brand_check:
        return fail(msg="Brand does not exist")
    if brand_check.name != post.name:
        check = await Brand.get_or_none(name=post.name)
        if check:
            return fail(msg=f"Brand name {check.name} exist!")

    data = post.dict()
    data.pop("id")
    await Brand.filter(pk=post.id).update(**data)
    return success(msg="Updated!")


@router.get("",
            summary="Brand List",
            response_model=brand.BrandListData,
            # dependencies=[Security(check_permissions, scopes=["brand_query"])]
            )
async def brand_list(
        pageSize: int = 10,
        current: int = 1,
        name: str = Query(None),
        seri_merk: str = Query(None),
        create_time: str = Query(None),
        update_time: str = Query(None),

):
    """
    Get All Brands
    :return:
    """
    # Query Conditions
    query = {}
    if name:
        query.setdefault('name__icontains', name)
    if seri_merk:
        query.setdefault('seri_merk', seri_merk)
    if create_time:
        query.setdefault('create_time__range', create_time)
    if update_time:
        query.setdefault('update_time__range', update_time)
        

    brand_data = Brand.annotate(key=F("id")).filter(**query).all()
    # Total
    total = await brand_data.count()
    # Query
    data = await brand_data.limit(pageSize).offset(pageSize * (current - 1)).order_by("-create_time") \
        .values(
        "key", "id", "name", "seri_merk", "create_time", "update_time")

    return res_antd(code=True, data=data, total=total)



@router.get("/dataBrand", summary="Get data brand")
async def dataBrand():
    data_brand = await Brand(family=1).all().values('name')

    if data_brand:
        new_dict = {}
        for item in data_brand:
            id = item['name']
            new_dict[id] = (item['name'])

        result = new_dict.items()
        return success(data=result)
    else:
        return fail(msg="Brand Not Found!")
    

@router.get("/seri", summary="Get data seri")
async def seri():
    seri = await Brand(family=1).all().values('seri_merk')

    if seri:
        new_dict = {}
        for item in seri:
            id = item['seri_merk']
            new_dict[id] = (item['seri_merk'])

        result = new_dict.items()
        return success(data=result)
    else:
        return fail(msg="Seri Not Found!")
