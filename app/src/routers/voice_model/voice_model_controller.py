from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.routers.voice_model.dto.create_voice_model_dto import CreateVoiceModelDto
from src.routers.voice_model.dto.voice_model_status_response_dto import (
    VoiceModelStatusResponseDto,
)
from src.routers.voice_model.dto.create_voice_sound_dto import CreateVoiceSoundDto
from src.utils.base_controller import BaseController


class VoiceModelController(BaseController):
    router = APIRouter(prefix="/voice-model", tags=["VoiceModel"])

    def get_router(self) -> APIRouter:
        self.router.post("/{user_id}")(self.create_model)
        self.router.get("{user_id}/status")(self.find_model_by_user_id)
        self.router.post("{user_id}/sound")(self.generate_sound_from_model)

        return self.router

    def create_model(
        self,
        user_id: str,
        create_voice_model_dto: CreateVoiceModelDto,
        authorization: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
    ):
        return ""

    def find_model_by_user_id(
        self,
        user_id: str,
        authorization: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
    ) -> VoiceModelStatusResponseDto:
        return VoiceModelStatusResponseDto(filepath="")

    def generate_sound_from_model(
        self,
        create_voice_model_dto: CreateVoiceSoundDto,
        authorization: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
    ):
        return ""
