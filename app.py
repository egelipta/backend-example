# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Maintainer: dgos
@Des: app运行时文件
"""

import json
from fastapi import FastAPI, Form, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from config import settings
from fastapi.staticfiles import StaticFiles
from core import Exception, Events, Router, Middleware
from fastapi.templating import Jinja2Templates
from tortoise.exceptions import OperationalError, DoesNotExist, IntegrityError, ValidationError
from fastapi.openapi.docs import (
    get_redoc_html, get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html)
from fastapi.openapi.utils import get_openapi

from core.Response import success

application = FastAPI(
    debug=settings.APP_DEBUG,
    docs_url=None,
    redoc_url=None,
    swagger_ui_oauth2_redirect_url=settings.SWAGGER_UI_OAUTH2_REDIRECT_URL,
)

# custom_openapi
def custom_openapi():
    if application.openapi_schema:
        return application.openapi_schema
    openapi_schema = get_openapi(
        description=settings.DESCRIPTION,
        version=settings.VERSION,
        title=settings.PROJECT_NAME,
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "/logo-teal.png"
    }
    application.openapi_schema = openapi_schema
    return application.openapi_schema


application.openapi = custom_openapi




@application.post("/api/callback/identify")
async def laporan_pintu(self):
    print("POST    ", self)
    return success(msg='')
# @application.post("/laporanpintu")
# async def laporan_pintu(event_log: str = Form(default=None)):
#     if (event_log):
#         try:
#             event_json = json.loads(event_log)

#             print(event_json)
#             # await Laporan_Pintu.filter(payload_json=event_json)
#             # event_log = event_log.json()

#             statusPintu = "Tertutup"
#             ipAddress = event_json['ipAddress']
#             subEventType = event_json['AccessControllerEvent']['subEventType']
#             # majorEventType = event_json['AccessControllerEvent']['majorEventType']
#             if (subEventType == 25):
#                 statusPintu = "Terbuka"
#             elif (subEventType == 26):
#                 statusPintu = "Tertutup"
#             elif (subEventType == 27):
#                 statusPintu = "Abnormally Open"
#             # print("ipAddress: ", ipAddress)

#             print(f"Pintu dengan alamat IP {ipAddress} {statusPintu}")

#             dataStatusPintu = await Status_Pintu.get_or_none(ip_address=ipAddress)
#             dataPintu = await Device.get_or_none(ip_address=ipAddress)
#             # responData = await Laporan_Pintu.get_or_none(respon=event_json)
#             if dataStatusPintu:
#                 # print("pintu ditemukan")
#                 await Status_Pintu.filter(ip_address=ipAddress).update(door_status=statusPintu)
#                 # await Laporan_Pintu.create(ipAddress=ipAddress, subEventType=subEventType)
#             else:
#                 # print("buat pintu")
#                 await Status_Pintu.create(
#                     ip_address=ipAddress, door_status=statusPintu, device_name=dataPintu.name)
#             # print("AccessControllerEvent: ",
#             #       event_log['AccessControllerEvent'])
#             # print("AccessControllerEvent.subEventType: ",
#             #       event_log['AccessControllerEvent']['subEventType'])

#         except Exception as e:
#             print("POST body from device is malformed: ", e)

#     return success(msg='')

# custom_swagger_ui_html


@application.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=application.openapi_url,
        title=application.title + " - Swagger UI",
        oauth2_redirect_url=application.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/swagger-ui-bundle.js",
        swagger_css_url="/swagger-ui.css",
    )


# swagger_ui_oauth2_redirect_url
@application.get(application.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


# redoc
@application.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=application.openapi_url,
        title=application.title + " - ReDoc",
        redoc_js_url="/redoc.standalone.js",
    )


# 事件监听
application.add_event_handler("startup", Events.startup(application))
application.add_event_handler("shutdown", Events.stopping(application))

# 异常错误处理
application.add_exception_handler(HTTPException, Exception.http_error_handler)
application.add_exception_handler(
    RequestValidationError, Exception.http422_error_handler)
application.add_exception_handler(
    Exception.UnicornException, Exception.unicorn_exception_handler)
application.add_exception_handler(DoesNotExist, Exception.mysql_does_not_exist)
application.add_exception_handler(
    IntegrityError, Exception.mysql_integrity_error)
application.add_exception_handler(
    ValidationError, Exception.mysql_validation_error)
application.add_exception_handler(
    OperationalError, Exception.mysql_operational_error)


# 中间件
application.add_middleware(Middleware.BaseMiddleware)

application.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

application.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY,
    session_cookie=settings.SESSION_COOKIE,
    max_age=settings.SESSION_MAX_AGE
)

# 路由
application.include_router(Router.router)

# 静态资源目录
application.mount(
    '/', StaticFiles(directory=settings.STATIC_DIR), name="static")
application.state.views = Jinja2Templates(directory=settings.TEMPLATE_DIR)

app = application
