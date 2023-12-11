from fastapi import APIRouter
import abc

from . import base_controller
from . import base_container


class BaseContainer(abc.ABC):
    controller: base_controller.BaseController
    containers: list["base_container.BaseContainer"] = []

    def get_router(self) -> APIRouter:
        return self.controller.get_router()
