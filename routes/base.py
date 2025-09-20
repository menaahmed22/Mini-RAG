from fastapi import FastAPI,APIRouter ,Depends
import os
from helpers.config import get_settings , Settings
base_router= APIRouter(
                    prefix="/api/v1", # this prefix should be added after URL
                    tags=["api_v1"]
)

@base_router.get("/")
async def welcome (app_setting : Settings =Depends (get_settings)) :
    App_Name = app_setting.APP_NAME
    App_Version = app_setting.APP_VERSION

    return {
        "app_name": App_Name,
        "app_version": App_Version,
    }
