# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:29 PM
@Author: me
@Des: layanan Schema
"""
from datetime import datetime
from pydantic import Field, BaseModel
from typing import List, Optional
from schemas.base import ResAntTable


class CreateLayanan(BaseModel):
    nomor_tiket: str = Field(max_length=255)
    jenis_layanan: str = Field(max_length=255)
    co_location: str = Field(max_length=255)
    # jenis_infra: str = Field(max_length=255)
    perangkat: str = Field(max_length=255)
    mulai_kunjungan: datetime
    akhir_kunjungan: datetime
    pemandu: Optional[str] = Field(max_length=255)
    status: Optional[int] 
    detail_tolak: Optional[str] = Field(max_length=255)


class UpdateLayanan(CreateLayanan):
    id: int

class TolakLayanan(BaseModel):
    detail_tolak: Optional[str] = Field(max_length=255)
    id: int


class LayananItem(UpdateLayanan):
    key: int
    id: int
    create_time: datetime
    update_time: datetime


class LayananDelete(BaseModel):
    id: List[int]


class LayananListData(ResAntTable):
    data: List[LayananItem]
