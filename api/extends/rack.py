# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: Rack
"""
import os
import time

from api.endpoints.common import write_access_log
from api.extends.sms import check_code
from core.Response import success, fail, res_antd
from models.rack import Rack
from schemas import rack
from core.Utils import en_password, check_password, random_str
from core.Auth import create_access_token, check_permissions
from fastapi import Request, Query, APIRouter, Security, File, UploadFile
from config import settings
from typing import List
from tortoise.queryset import F


router = APIRouter(prefix='/rack')


@router.get("",
            summary="Rack List",
            response_model=rack.RackListData,
            # dependencies=[Security(check_permissions, scopes=["rack_query"])]
            )
async def rack_list(
        name: str = Query(None),
        posx: int = Query(None),
        posy: int = Query(None),
        posz: int = Query(None),
        width: int = Query(None),
        height: int = Query(None),
        depth: int = Query(None),
        create_time: str = Query(None),
        update_time: str = Query(None),


):
    """
    Get All Racks
    :return:
    """
    # Query Conditions
    query = {}
    if name:
        query.setdefault('name__icontains', name)
    if posx:
        query.setdefault('posx', posx)
    if posy:
        query.setdefault('posy', posy)
    if posz:
        query.setdefault('posz', posz)
    if width:
        query.setdefault('width', width)
    if height:
        query.setdefault('height', height) 
    if depth:
        query.setdefault('depth', depth)  
    if create_time:
        query.setdefault('create_time__range', create_time)
    if update_time:
        query.setdefault('update_time__range', update_time)
        

    rack_data = Rack.annotate(key=F("id")).filter(**query).all()
    # Total
    total = await rack_data.count()
    # Query
    data = await rack_data.order_by("-create_time") \
        .values(
        "key", "id", "name", "posx","posy","posz", "width", "height", "depth", "create_time", "update_time")
    

    return res_antd(code=True, data=data, total=total)

