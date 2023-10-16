# -*- coding:utf-8 -*-
"""
@Time : 2022/4/24 10:40 AM
@Author: me
@Des: layanan model
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


class Layanan(TimestampMixin):
    nomor_tiket = fields.CharField(default='', max_length=255)
    jenis_layanan = fields.CharField(
        default='', max_length=255)
    co_location = fields.CharField(default='', max_length=255)
    # jenis_infra = fields.CharField(
    #     default='', max_length=255)
    perangkat = fields.CharField(max_length=255)
    mulai_kunjungan = fields.DatetimeField()
    akhir_kunjungan = fields.DatetimeField()
    pemandu = fields.CharField(null=True, max_length=255)
    status = fields.CharField(default=0, max_length=11)
    detail_tolak = fields.CharField(null=True, max_length=255)
    # status = fields.IntField(default=0, null=True,
    #                          description='0 Belum Masuk, 1 Sudah Masuk, 2 Sedang Di Dalam, and 3 Sudah Keluar')
   
    class Meta:
        table_description = "Layanan Table"
        table = "layanan"
