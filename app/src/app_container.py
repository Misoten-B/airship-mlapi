from typing import Callable
from fastapi import APIRouter
from src.routers.voice_model.voice_model_container import VoiceModelContainer
from src.utils.base_container import BaseContainer

from src.app_controller import AppController


class AppContainer(BaseContainer):
    def __init__(self) -> None:
        self.controller = AppController()
        self.containers.append(VoiceModelContainer())

    def include_routers(self, delegate_func: Callable[[APIRouter], None]) -> None:
        for container in self.containers:
            delegate_func(container.controller.get_router())
