# -*- coding:utf-8 -*-
"""
@Time : 2022/4/24 10:15 AM
@Maintainer: dgos
@Des: mysql database
"""

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import os


# -----------------------Database configuration-----------------------------------
DB_ORM_CONFIG = {
    "connections": {
        "base": {
            'engine': 'tortoise.backends.mysql',
            "credentials": {
                'host': os.getenv('DEV_BASE_HOST', 'localhost'),
                'user': os.getenv('DEV_MYSQL_USER', 'root'),
                'password': os.getenv('DEV_MYSQL_PASSWORD', 'pjvmsrootpass213'),
                'port': os.getenv('DEV_MYSQL_PORT', '3306'),
                'database': os.getenv('DEV_MYSQL_DATABASE_NAME', 'dcoss23'),
            }
        }

    },
    "apps": {
        "base": {"models": ["models.base"], "default_connection": "base"},
        "layanan": {"models": ["models.layanan"], "default_connection": "base"},
        "aset": {"models": ["models.aset"], "default_connection": "base"},
        "daftar_pengunjung": {"models": ["models.daftar_pengunjung"], "default_connection": "base"},
        "buku_tamu": {"models": ["models.buku_tamu"], "default_connection": "base"},
        "merek_tipe": {"models": ["models.merek_tipe"], "default_connection": "base"},
        "pemandu": {"models": ["models.pemandu"], "default_connection": "base"},
        "lokasi": {"models": ["models.lokasi"], "default_connection": "base"},
        "power": {"models": ["models.power"], "default_connection": "base"},
        "pengunjung_hadir": {"models": ["models.pengunjung_hadir"], "default_connection": "base"},
        "pakai_aset": {"models": ["models.pakai_aset"], "default_connection": "base"},
        "rack": {"models": ["models.rack"], "default_connection": "base"},
    },
    'use_tz': True,
    'timezone': 'Asia/Jakarta'
}


async def register_mysql(app: FastAPI):
    # Register database
    register_tortoise(
        app,
        config=DB_ORM_CONFIG,
        generate_schemas=False,
        add_exception_handlers=False,
    )
