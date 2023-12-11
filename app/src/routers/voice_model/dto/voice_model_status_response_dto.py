from pydantic import BaseModel


class VoiceModelStatusResponseDto(BaseModel):
    filepath: str
