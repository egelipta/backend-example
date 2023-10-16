# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: lokasi
"""

from datetime import datetime
from pydantic import Field, BaseModel, validator
from typing import Optional, List
from schemas.base import BaseResp, ResAntTable


class CreatePower(BaseModel):
    nama: Optional[str] = Field(max_length=255)
    lokasi: Optional[str] = Field(max_length=255)
    nama_ruangan: Optional[str] = Field(max_length=255)
    posisi_rak: Optional[str] = Field(max_length=255)
    source: Optional[str] = Field(max_length=1)
    power: Optional[str] = Field(max_length=255)
    tipe: Optional[str] = Field(max_length=255)
    sn_aset: Optional[str] = Field(max_length=255)

class InsertPower(BaseModel):
    nama: Optional[str] = Field(max_length=255)
    lokasi: Optional[str] = Field(max_length=255)
    nama_ruangan: Optional[str] = Field(max_length=255)
    posisi_rak: Optional[str] = Field(max_length=255)
    source: Optional[str] = Field(max_length=1)
    # power: Optional[str] = Field(max_length=255)
    tipe: List[str]
    jumlah: List[int]

class PutPower(BaseModel):
    id: List[int]
    sn_aset: str
    


class UpdatePower(CreatePower):
    id: int


class PowerItem(UpdatePower):
    key: int
    id: int
    create_time: datetime
    update_time: datetime


class PowerDelete(BaseModel):
    id: int


class PowerListData(ResAntTable):
    data: List[PowerItem]


