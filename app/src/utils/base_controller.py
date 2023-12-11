from abc import ABC, abstractmethod
from fastapi import APIRouter


class BaseController(ABC):
    @abstractmethod
    def get_router(self) -> APIRouter:
        raise NotImplementedError
