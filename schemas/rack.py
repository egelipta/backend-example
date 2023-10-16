# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:29 PM
@Author: me
@Des: aset Schema
"""
from datetime import datetime
from pydantic import Field, BaseModel
from typing import List
from schemas.base import ResAntTable


class CreateRack(BaseModel):
    name: str = Field(max_length=100)
    posx: int
    posy: int
    posz: int
    width: int
    height: int
    depth: int


class UpdateRack(CreateRack):
    id: int


class RackItem(UpdateRack):
    key: int
    id: int
    create_time: datetime
    update_time: datetime


class RackDelete(BaseModel):
    id: List[int]


class RackListData(ResAntTable):
    data: List[RackItem]

