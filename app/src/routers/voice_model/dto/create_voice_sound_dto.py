from pydantic import BaseModel


class CreateVoiceSoundDto(BaseModel):
    filepath: str
