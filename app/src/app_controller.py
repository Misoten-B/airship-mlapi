import fastapi
from fastapi import APIRouter
from src.utils.base_controller import BaseController


class AppController(BaseController):
    router = fastapi.APIRouter()

    def get_router(self) -> APIRouter:
        return self.router

    @router.get("/")
    async def _hello_fast_api():
        return "Hello FastAPI"
