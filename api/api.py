# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Maintainer: dgos
@Des: api路由
"""
from fastapi import APIRouter
from api.endpoints.test import test_oath2
from api.endpoints import user, role, access, websocket
from api.extends import daftar_pengunjung, sms, cos, aset, layanan, buku_tamu, merek_tipe, pemandu, lokasi, power, pengunjung_hadir, pakai_aset, rack


api_router = APIRouter(prefix="/api/v1")
api_router.post("/test/oath2", tags=["Test Oath2 authorization"])(test_oath2)
api_router.include_router(user.router, prefix='/admin',
                          tags=["User Management"])
api_router.include_router(role.router, prefix='/admin',
                          tags=["Role management"])
api_router.include_router(access.router, prefix='/admin',
                          tags=["authority management"])
api_router.include_router(websocket.router, prefix='/ws', tags=["WebSocket"])
api_router.include_router(sms.router, prefix='/sms', tags=["SMS interface"])
api_router.include_router(cos.router, prefix='/cos',
                          tags=["Object storage interface"])
api_router.include_router(
    layanan.router, prefix='/layanan', tags=["Layanan"])
api_router.include_router(
    aset.router, prefix='/aset', tags=["Aset"])
api_router.include_router(
    daftar_pengunjung.router, prefix='/daftar_pengunjung', tags=["Daftar Pengunjung"])
api_router.include_router(
    buku_tamu.router, prefix='/buku_tamu', tags=["Buku Tamu"])
api_router.include_router(
    merek_tipe.router, prefix='/merek_tipe', tags=["MerekTipe"])
api_router.include_router(
    pemandu.router, prefix='/pemandu', tags=["Pemandu"])
api_router.include_router(
    lokasi.router, prefix='/lokasi', tags=["Lokasi"])
api_router.include_router(
    power.router, prefix='/power', tags=["Power"])
api_router.include_router(
    pengunjung_hadir.router, prefix='/pengunjung_hadir', tags=["pengunjung_hadir"])
api_router.include_router(
    pakai_aset.router, prefix='/pakai_Aset', tags=["pakai_aset"])
api_router.include_router(
    rack.router, prefix='/pakai_Aset', tags=["rack"])
