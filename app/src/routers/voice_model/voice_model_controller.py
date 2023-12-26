from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.lib.azure.storage.blob_storage_client import BlobStorageClient
from src.routers.voice_model.voice_model_service import VoiceModelService
from src.routers.voice_model.dto.create_voice_model_dto import CreateVoiceModelDto
from src.routers.voice_model.dto.create_voice_sound_dto import CreateVoiceSoundDto
from src.utils.base_controller import BaseController
from src.utils.auth import verify_bearer_token
from src.utils.error.core import ResourceConflictException, ResourceNotFoundException


class VoiceModelController(BaseController):
    router = APIRouter(prefix="/voice-model", tags=["VoiceModel"])
    voice_model_service: VoiceModelService

    def __init__(self, voice_model_service: VoiceModelService) -> None:
        super().__init__()
        self.voice_model_service = voice_model_service

    def get_router(self) -> APIRouter:
        self.router.post("/{user_id}")(self.create_model)
        self.router.post("/{user_id}/sound")(self.generate_sound_from_model)

        return self.router

    def create_model(
        self,
        user_id: str,
        create_voice_model_dto: CreateVoiceModelDto,
        # authorization: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
    ):
        # token_str = authorization.credentials
        # is_autorized = verify_bearer_token(token_str)
        # if not is_autorized:
        #     raise HTTPException(401)
        
        dto = create_voice_model_dto
        try:
            self.voice_model_service.create_model(
                user_id,dto
            )
        except ResourceConflictException as e:
            raise HTTPException(409,e.target)
        except ResourceNotFoundException as e:
            raise HTTPException(404,e.target)
        except Exception as e:
            raise HTTPException(500,f"{e.__class__.__name__}: {e.args}")


    def generate_sound_from_model(
        self,
        user_id: str,
        create_voice_sound_dto: CreateVoiceSoundDto,
        # authorization: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
    ):
        # token_str = authorization.credentials
        # is_autorized = verify_bearer_token(token_str)
        # if not is_autorized:
        #     raise HTTPException(401)

        dto = create_voice_sound_dto
        try:
            self.voice_model_service.create_sound_from_model(
                user_id, dto
            )

        except ResourceConflictException as e:
            raise HTTPException(409,e.target)
        except ResourceNotFoundException as e:
            raise HTTPException(404,e.target)
            
