# -*- coding:utf-8 -*-
"""
@Time : 2022/4/27 5:29 PM
@Author: me
@Des: employee Schema
"""
from datetime import datetime
from pydantic import Field, BaseModel, validator
from typing import Optional, List
from schemas.base import BaseResp, ResAntTable


class CreatePemandu(BaseModel):
    nama: str = Field(min_length=1, max_length=255)
    no_hp: Optional[str] = Field(max_length=255)
    
 
class UpdatePemandu(CreatePemandu):
    id: int

    

class PemanduItem(UpdatePemandu):
    key: int
    id: int
    create_time: datetime
    update_time: datetime
    no_hp: Optional[str] = Field(max_length=255)
    nama: Optional[str] = Field(max_length=255)
    

class PemanduDelete(BaseModel):
    id: List[int]




class PemanduListData(ResAntTable):
    data: List[PemanduItem]


