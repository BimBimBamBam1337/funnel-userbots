from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from loguru import logger

__all__ = ("router",)

router = APIRouter(
    route_class=DishkaRoute,
)

@router.post("/auth_userbot")
async def auth_userbot_route()
