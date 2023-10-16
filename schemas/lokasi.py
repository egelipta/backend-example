# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: Lokasi
"""

from datetime import datetime
from pydantic import Field, BaseModel, validator
from typing import Optional, List
from schemas.base import BaseResp, ResAntTable


class CreateLokasi(BaseModel):
    lokasi: str = Field(max_length=255)
    nama_ruangan: Optional[str] = Field(max_length=255)
    posisi_rak: Optional[str] = Field(max_length=255)
    posisi_u: Optional[str] = Field(max_length=255)
    sn_aset: Optional[str] = Field(max_length=255)


class UpdateLokasi(CreateLokasi):
    id: int


class LokasiItem(UpdateLokasi):
    key: int
    id: int
    create_time: datetime
    update_time: datetime


class LokasiDelete(BaseModel):
    id: int


class LokasiListData(ResAntTable):
    data: List[LokasiItem]


