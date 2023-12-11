from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.routers.voice_model.voice_model_service import VoiceModelService
from src.routers.voice_model.dto.create_voice_model_dto import CreateVoiceModelDto
from src.routers.voice_model.dto.create_voice_sound_dto import CreateVoiceSoundDto
from src.utils.base_controller import BaseController
from src.utils.auth import verify_bearer_token


class VoiceModelController(BaseController):
    router = APIRouter(prefix="/voice-model", tags=["VoiceModel"])
    voice_model_service: VoiceModelService

    def __init__(self, voice_model_service: VoiceModelService) -> None:
        super().__init__()
        self.voice_model_service = voice_model_service

    def get_router(self) -> APIRouter:
        self.router.post("/{user_id}")(self.create_model)
        self.router.post("{user_id}/sound")(self.generate_sound_from_model)

        return self.router

    def create_model(
        self,
        user_id: str,
        create_voice_model_dto: CreateVoiceModelDto,
        authorization: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
    ):
        token_str = authorization.credentials
        is_autorized = verify_bearer_token(token_str)
        if not is_autorized:
            raise HTTPException(401)
        dto = create_voice_model_dto
        self.voice_model_service.create_model(user_id, dto.file_name, dto.language)

    def generate_sound_from_model(
        self,
        user_id: str,
        create_voice_sound_dto: CreateVoiceSoundDto,
        authorization: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
    ):
        token_str = authorization.credentials
        is_autorized = verify_bearer_token(token_str)
        if not is_autorized:
            raise HTTPException(401)

        dto = create_voice_sound_dto
        self.voice_model_service.create_sound_from_model(
            user_id, dto.file_name, dto.language
        )
