from pydantic import BaseModel, Field

from src.routers.voice_model.language_entity import Language


class CreateVoiceModelDto(BaseModel):
    train_sound_file_name: str=Field(examples=["filename.wav"])
    language: Language
