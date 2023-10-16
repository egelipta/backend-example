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


class Psu(TimestampMixin):
    power = fields.IntField(min=0)
    tipe_socket = fields.CharField(default='', max_length=255)
    id_aset = fields.IntField(min=0)
    
    # status = fields.IntField(default=0, null=True,
    #                          description='0 Belum Masuk, 1 Sudah Masuk, 2 Sedang Di Dalam, and 3 Sudah Keluar')
   
    class Meta:
        table_description = "Psu Table"
        table = "psu"
