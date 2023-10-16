# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:29 PM
@Author: me
@Des: aset Schema
"""
from datetime import datetime
from pydantic import Field, BaseModel
from typing import List, Optional
from schemas.base import ResAntTable


class CreateAset(BaseModel):
    merek: str = Field(max_length=255)
    tipe: str = Field(max_length=255)
    fungsi_perangkat: str = Field(max_length=25)
    foto_perangkat: str = Field(max_length=255)
    nomor_seri: str = Field(max_length=255)
    jenis_infra: str = Field(max_length=255)
    instansi_pemilik: str = Field(max_length=255)
    penanggung_jawab: str = Field(max_length=255)
    lokasi: str = Field(max_length=255)
    nama_ruangan: str = Field(max_length=255)
    posisi_rak: str = Field(max_length=255)
    psu: str = Field(max_length=255)
    posisi_u: str = Field(max_length=255)
    power: str = Field(max_length=255)
    kapasitas_cpu: str = Field(max_length=255)
    kapasitas_hdd: str = Field(max_length=255)
    kapasitas_ram: str = Field(max_length=255)
    daya: str = Field(max_length=255)
    tanggal_pemasangan: Optional[datetime] = None
    tanggal_penarikan: Optional[datetime] = None
    keterangan: Optional[str] = Field(max_length=255)
    status_aset: int
    user: str = Field(max_length=255)


class UpdateAset(CreateAset):
    id: int


class AsetItem(UpdateAset):
    key: int
    id: int
    create_time: datetime
    update_time: datetime


class AsetDelete(BaseModel):
    id: List[int]


class AsetListData(ResAntTable):
    data: List[AsetItem]


class UpdateStatusAset(BaseModel):
    id: int
    status_aset: bool
    tanggal_penarikan: Optional[datetime]
    nomor_seri: Optional[str] = Field(max_length=255)


