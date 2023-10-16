# -*- coding:utf-8 -*-
"""
@Time : 2022/4/24 10:40 AM
@Author: me
@Des: systemInfo model
"""

from tortoise import fields
from tortoise.models import Model

# class TimestampMixin(Model):
#     create_time = fields.DatetimeField(auto_now_add=True, description='created at')
#     update_time = fields.DatetimeField(auto_now=True, description="updated at")

    # class Meta:
    #     abstract = True
        
class SystemInfo(Model):
    software_name = fields.CharField(default='', max_length=255, description='software_name')
    version = fields.CharField(default='', max_length=255, description='version')
    system = fields.CharField(default='', max_length=25, description='system')
    jdk_version = fields.CharField(null=False, max_length=255, description="jdk_version")
    database_type = fields.CharField(null=False, max_length=255, description="database_type")
    database_port = fields.CharField(null=False, max_length=255, description="database_port")
    # fields.OneToOneField("base.SystemInfo", related_name="device", on_delete=fields.CASCADE)

    class Meta:
        table_description = "SystemInfo Table"
        table = "systemInfo"
