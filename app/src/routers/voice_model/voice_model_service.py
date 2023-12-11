from src.routers.voice_model.language_entity import Language
from vall_e_x.app import make_npz_prompt, infer_from_prompt


class VoiceModelService:
    def create_model(self, user_id: str, output_file_name: str, language: Language):
        raise NotImplementedError()

    def create_sound_from_model(
        self, user_id: str, output_file_name: str, language: Language
    ):
        raise NotImplementedError()
