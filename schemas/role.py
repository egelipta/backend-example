# -*- coding:utf-8 -*-
"""
@Time : 2022/5/15 11:52 PM
@Maintainer: dgos
@Des: role schemas
"""
from pydantic import BaseModel, Field
from typing import List, Optional
from schemas.base import ResAntTable
from datetime import datetime


class CreateRole(BaseModel):
    role_name: str = Field(min_length=3, max_length=25)
    role_status: Optional[bool] = False
    role_desc: Optional[str] = Field(max_length=255)


class UpdateRole(BaseModel):
    id: int
    role_name: str
    role_status: Optional[bool]
    role_desc: Optional[str]


class RoleItem(BaseModel):
    id: int
    key: int
    role_name: str
    role_status: Optional[bool]
    role_desc: Optional[str]
    create_time: datetime
    update_time: datetime


class RoleList(ResAntTable):
    data: List[RoleItem]


class SetAccess(BaseModel):
    role_id: int
    access: List[int] = Field(default=[], description="Permissions")


class CreateAccess(BaseModel):
    access_name: str = Field("test", description="Permission name")
    scopes: str = Field("test", description="Permissions")
    parent_id: int = 0
    is_check: bool = False
    is_menu: bool = False
