from pydantic import BaseModel

from src.routers.voice_model.language_entity import Language


class CreateVoiceSoundDto(BaseModel):
    content: str
    file_name: str
    language: Language
