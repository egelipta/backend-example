# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:24 PM
@Author: me
@Des: MerekTipe
"""

from datetime import datetime
from pydantic import Field, BaseModel, validator
from typing import Optional, List
from schemas.base import BaseResp, ResAntTable


class CreateMerekTipe(BaseModel):
    merek: str = Field(max_length=255)
    tipe: Optional[str] = Field(max_length=255)

class UpdateMerekTipe(CreateMerekTipe):
    id: int


class MerekTipeItem(UpdateMerekTipe):
    key: int
    id: int
    create_time: datetime
    update_time: datetime


class MerekTipeDelete(BaseModel):
    id: int


class MerekTipeListData(ResAntTable):
    data: List[MerekTipeItem]


