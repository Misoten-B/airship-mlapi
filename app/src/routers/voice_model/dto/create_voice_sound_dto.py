from pydantic import BaseModel, Field

from src.routers.voice_model.language_entity import Language


class CreateVoiceSoundDto(BaseModel):
    content: str=Field(examples=["しゃべらせる内容です。"])
    output_file_name: str=Field(examples=["filename.wav"])
    language: Language
