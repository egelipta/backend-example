# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: MerekTipe Management
"""

from tortoise import fields
from tortoise.models import Model

class TimestampMixin(Model):
    create_time = fields.DatetimeField(auto_now_add=True, description='created at')
    update_time = fields.DatetimeField(auto_now=True, description="updated at")

    class Meta:
        abstract = True
        
class Lokasi(TimestampMixin):
    lokasi = fields.CharField(default='', max_length=255)
    nama_ruangan = fields.CharField(default='', max_length=255)
    posisi_rak = fields.CharField(default='', max_length=255)
    posisi_u = fields.CharField(default='', max_length=255)
    sn_aset = fields.CharField(default='', max_length=255)


    class Meta:
        table_description = "Lokasi Table"
        table = "lokasi"