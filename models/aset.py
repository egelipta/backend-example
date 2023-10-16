# -*- coding:utf-8 -*-
"""
@Time : 2022/4/24 10:40 AM
@Author: me
@Des: aset model
"""

from typing import List
from tortoise import fields
from tortoise.models import Model

class TimestampMixin(Model):
    create_time = fields.DatetimeField(
        auto_now_add=True, description='created at')
    update_time = fields.DatetimeField(auto_now=True, description="updated at")

    class Meta:
        abstract = True


class Aset(TimestampMixin):
    merek = fields.CharField(default='', max_length=255)
    tipe = fields.CharField(default='', max_length=255)
    fungsi_perangkat = fields.CharField(
        default='', max_length=255)
    foto_perangkat = fields.CharField(default='', max_length=255)
    nomor_seri = fields.CharField(
        default='', max_length=255)
    jenis_infra = fields.CharField(max_length=255)
    instansi_pemilik = fields.CharField(max_length=255)
    penanggung_jawab = fields.CharField(max_length=255)
    lokasi = fields.CharField(max_length=255)
    nama_ruangan = fields.CharField(max_length=255)
    posisi_rak = fields.CharField(max_length=255)
    psu = fields.CharField(max_length=255)
    posisi_u = fields.CharField(max_length=255)
    power = fields.CharField(max_length=255)
    kapasitas_cpu = fields.CharField(max_length=255)
    kapasitas_hdd = fields.CharField(max_length=255)
    kapasitas_ram = fields.CharField(max_length=255)
    daya = fields.CharField(max_length=255)    
    tanggal_pemasangan = fields.DatetimeField(null=True)
    tanggal_penarikan = fields.DatetimeField(null=True)
    keterangan = fields.CharField(max_length=255, null=True)
    status_aset = fields.IntField()
    user = fields.CharField(max_length=255)

    # status = fields.IntField(default=0, null=True,
    #                          description='0 Belum Masuk, 1 Sudah Masuk, 2 Sedang Di Dalam, and 3 Sudah Keluar')
   
    class Meta:
        table_description = "Aset Table"
        table = "aset"
