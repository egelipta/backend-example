# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: Daftar Pengunjung
"""

from tortoise import fields
from tortoise.models import Model

class TimestampMixin(Model):
    create_time = fields.DatetimeField(auto_now_add=True, description='created at')
    update_time = fields.DatetimeField(auto_now=True, description="updated at")

    class Meta:
        abstract = True
        
class DaftarPengunjung(TimestampMixin):
    nik = fields.CharField(default='', max_length=255)
    nama = fields.CharField(default='', max_length=255)
    status = fields.CharField(default='', max_length=255)
    instansi = fields.CharField(default='', max_length=255)
    foto = fields.CharField(default='', max_length=255)

    class Meta:
        table_description = "Daftar Pengunjung Table"
        table = "daftar_pengunjung"