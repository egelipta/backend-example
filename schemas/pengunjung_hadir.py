# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: PengunjungHadir
"""

from datetime import datetime
from pydantic import Field, BaseModel, validator
from typing import Optional, List
from schemas.base import BaseResp, ResAntTable


class CreatePengunjungHadir(BaseModel):
    nomor_tiket: str = Field(max_length=255)
    nik: str = Field(max_length=255)
    hadir: Optional[str] = Field(max_length=255)
    

class UpdatePengunjungHadir(CreatePengunjungHadir):
    id: int


class PengunjungHadirItem(UpdatePengunjungHadir):
    key: int
    id: int
    create_time: datetime
    update_time: datetime


class PengunjungHadirDelete(BaseModel):
    id: int


class PengunjungHadirListData(ResAntTable):
    data: List[PengunjungHadirItem]

class InsertAkanHadir(BaseModel):
    # power: Optional[str] = Field(max_length=255)
    nomor_tiket: str
    nik: List[str]

#-------------------------------
# class CreatePengunjungHadir(BaseModel):
#     no_tiket: str = Field(max_length=255)
#     jam_masuk: datetime
#     jam_keluar: datetime
#     laporan_pekerjaan: str = Field(max_length=255)
#     daftar_pengunjung: List[str]

# class UpdatePengunjungHadir(CreatePengunjungHadir):
#     id: int


# class PengunjungHadirItem(UpdatePengunjungHadir):
#     key: int
#     id: int
#     create_time: datetime
#     update_time: datetime


# class PengunjungHadirDelete(BaseModel):
#     id: int


# class PengunjungHadirListData(ResAntTable):
#     data: List[PengunjungHadirItem]