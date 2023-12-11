from src.routers.voice_model.voice_model_controller import VoiceModelController
from src.utils.base_container import BaseContainer


class VoiceModelContainer(BaseContainer):
    def __init__(self) -> None:
        super().__init__()
        self.controller = VoiceModelController()
