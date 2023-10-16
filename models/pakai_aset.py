# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: BukuTamu Management
"""

from tortoise import fields
from tortoise.models import Model

class TimestampMixin(Model):
    create_time = fields.DatetimeField(auto_now_add=True, description='created at')
    update_time = fields.DatetimeField(auto_now=True, description="updated at")

    class Meta:
        abstract = True
        
class PakaiAset(TimestampMixin):
    nomor_tiket = fields.CharField(default='', max_length=255)
    nomor_seri = fields.CharField(default='', max_length=255)
    
   

    class Meta:
        table_description = "BukuTamu Table"
        table = "pakai_aset"

#-------------------

# from tortoise import fields
# from tortoise.models import Model

# class TimestampMixin(Model):
#     create_time = fields.DatetimeField(auto_now_add=True, description='created at')
#     update_time = fields.DatetimeField(auto_now=True, description="updated at")

#     class Meta:
#         abstract = True

# class BukuTamu(TimestampMixin):
#     no_tiket = fields.CharField(default='', max_length=255)
#     jam_masuk = fields.DatetimeField(auto_now_add=True)
#     jam_keluar = fields.DatetimeField(auto_now=True)
#     laporan_pekerjaan = fields.CharField(default='', max_length=255)
#     daftar_pengunjung = fields.JSONField(default=list)

#     class Meta:
#         table_description = "BukuTamu Table"
#         table = "pengunjung_hadir"