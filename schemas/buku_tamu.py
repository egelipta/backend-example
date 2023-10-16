# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: BukuTamu
"""

from datetime import datetime
from pydantic import Field, BaseModel, validator
from typing import Optional, List
from schemas.base import BaseResp, ResAntTable


class CreateBukuTamu(BaseModel):
    no_tiket: str = Field(max_length=255)
    jam_masuk: datetime
    jam_keluar: datetime
    laporan_pekerjaan: str = Field(max_length=255)
    daftar_pengunjung: str = Field(max_length=255)

class UpdateBukuTamu(CreateBukuTamu):
    id: int


class BukuTamuItem(UpdateBukuTamu):
    key: int
    id: int
    create_time: datetime
    update_time: datetime


class BukuTamuDelete(BaseModel):
    id: int


class BukuTamuListData(ResAntTable):
    data: List[BukuTamuItem]

#-------------------------------
# class CreateBukuTamu(BaseModel):
#     no_tiket: str = Field(max_length=255)
#     jam_masuk: datetime
#     jam_keluar: datetime
#     laporan_pekerjaan: str = Field(max_length=255)
#     daftar_pengunjung: List[str]

# class UpdateBukuTamu(CreateBukuTamu):
#     id: int


# class BukuTamuItem(UpdateBukuTamu):
#     key: int
#     id: int
#     create_time: datetime
#     update_time: datetime


# class BukuTamuDelete(BaseModel):
#     id: int


# class BukuTamuListData(ResAntTable):
#     data: List[BukuTamuItem]