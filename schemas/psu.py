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


class CreatePsu(BaseModel):
    power: int
    tipe_socket: str = Field(max_length=100)
    id_aset: int


class UpdatePsu(CreatePsu):
    id: int


class PsuItem(UpdatePsu):
    key: int
    id: int
    create_time: datetime
    update_time: datetime


class PsuDelete(BaseModel):
    id: List[int]


class PsuListData(ResAntTable):
    data: List[PsuItem]

