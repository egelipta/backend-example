# -*- coding:utf-8 -*-
"""
@Time : 2022/4/24 10:40 AM
@Author: me
@Des: Rack model
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


class Rack(TimestampMixin):
    name = fields.CharField(default='', max_length=255)
    posx = fields.IntField(max=11)
    posy = fields.IntField(max=11)
    posz = fields.IntField(max=11)
    width = fields.IntField(max=11)
    height = fields.IntField(max=11)
    depth = fields.IntField(max=11)
    class Meta:
        table_description = "Rack Table"
        table = "rack"
