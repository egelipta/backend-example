# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: PakaiAset
"""

from datetime import datetime
from pydantic import Field, BaseModel, validator
from typing import Optional, List
from schemas.base import BaseResp, ResAntTable


class CreatePakaiAset(BaseModel):
    nomor_tiket: str = Field(max_length=255)
    nomor_seri: str = Field(max_length=255)
    
    

class UpdatePakaiAset(CreatePakaiAset):
    id: int


class PakaiAsetItem(UpdatePakaiAset):
    key: int
    id: int
    create_time: datetime
    update_time: datetime


class PakaiAsetDelete(BaseModel):
    id: int


class PakaiAsetListData(ResAntTable):
    data: List[PakaiAsetItem]

class InsertAkanPakaiAset(BaseModel):
    # power: Optional[str] = Field(max_length=255)
    nomor_tiket: str
    nomor_seri: List[str]

#-------------------------------
# class CreatePakaiAset(BaseModel):
#     no_tiket: str = Field(max_length=255)
#     jam_masuk: datetime
#     jam_keluar: datetime
#     laporan_pekerjaan: str = Field(max_length=255)
#     daftar_pengunjung: List[str]

# class UpdatePakaiAset(CreatePakaiAset):
#     id: int


# class PakaiAsetItem(UpdatePakaiAset):
#     key: int
#     id: int
#     create_time: datetime
#     update_time: datetime


# class PakaiAsetDelete(BaseModel):
#     id: int


# class PakaiAsetListData(ResAntTable):
#     data: List[PakaiAsetItem]