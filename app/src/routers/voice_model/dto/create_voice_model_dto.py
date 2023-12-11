from pydantic import BaseModel

from src.routers.voice_model.language_entity import Language


class CreateVoiceModelDto(BaseModel):
    filepath: str
    language:Language
