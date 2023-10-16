# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:29 PM
@Author: me
@Des: systemInfo Schema
"""
from datetime import datetime
from pydantic import Field, BaseModel, validator
from typing import Optional, List
from schemas.base import BaseResp, ResAntTable


# class CreateDevice(BaseModel):
#     name: str = Field(min_length=1, max_length=255)
#     family: str = Field(min_length=1, max_length=255)
#     ip_address: str = Field(min_length=1, max_length=25)
#     username: str = Field(min_length=1, max_length=255)
#     password: str = Field(min_length=1, max_length=255)
    

# class UpdateDevice(CreateDevice):
#     id: int


class SystemInfo(BaseModel):
    software_name: str
    version: str
    system: str
    jdk_version: str
    database_type: str
    database_port: str


# class DeviceDelete(BaseModel):
#     id: List[int]




class SystemInfoList(ResAntTable):
    data: List[SystemInfo]


