# -*- coding:utf-8 -*-
"""
@Time : 2022/4/24 10:40 AM
@Author: me
@Des: employee model
"""

from tortoise import fields
from tortoise.models import Model

class TimestampMixin(Model):
    create_time = fields.DatetimeField(auto_now_add=True, description='created at')
    update_time = fields.DatetimeField(auto_now=True, description="updated at")

    class Meta:
        abstract = True
        
class Pemandu(TimestampMixin):
    nama = fields.CharField(default='', max_length=255, description='nama')
    no_hp = fields.CharField(default='', max_length=255, description="no_hp")
    # fields.OneToOneField("base.Pemandu", related_nama="employee", on_delete=fields.CASCADE)
    class Meta:
        table_description = "Pemandu Table"
        table = "pemandu"
