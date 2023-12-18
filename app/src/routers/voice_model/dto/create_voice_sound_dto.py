from uuid import uuid4
from pydantic import BaseModel, Field

from src.routers.voice_model.language_entity import Language


class CreateVoiceSoundDto(BaseModel):
    content: str=Field(examples=["しゃべらせる内容です。"])
    ar_assets_id: str=Field(examples=[uuid4()])
    language: Language
