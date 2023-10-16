# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: DaftarPengunjung Management
"""

from datetime import datetime
from pydantic import Field, BaseModel
from typing import List
from schemas.base import ResAntTable


class CreateDaftarPengunjung(BaseModel):
    nik: str = Field(max_length=255)
    nama: str = Field(max_length=255)
    status: str = Field(max_length=255)
    instansi: str = Field(max_length=255)
    foto: str = Field(max_length=255)

class UpdateDaftarPengunjung(CreateDaftarPengunjung):
    id: int


class DaftarPengunjungItem(UpdateDaftarPengunjung):
    key: int
    id: int
    create_time: datetime
    update_time: datetime


class DaftarPengunjungDelete(BaseModel):
    id: int


class DaftarPengunjungListData(ResAntTable):
    data: List[DaftarPengunjungItem]


