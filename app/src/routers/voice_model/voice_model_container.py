from src.routers.voice_model.voice_model_service import VoiceModelService
from src.routers.voice_model.voice_model_controller import VoiceModelController
from src.utils.base_container import BaseContainer


class VoiceModelContainer(BaseContainer):
    voice_model_service: VoiceModelService

    def __init__(self) -> None:
        super().__init__()
        self.voice_model_service = VoiceModelService()
        self.controller = VoiceModelController(self.voice_model_service)
