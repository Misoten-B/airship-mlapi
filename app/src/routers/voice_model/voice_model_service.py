import io
import os
import httpx
from soundfile import read,write
from src.routers.voice_model.dto.create_voice_model_dto import CreateVoiceModelDto
from src.routers.voice_model.dto.create_voice_sound_dto import CreateVoiceSoundDto
from src.lib.azure.storage.blob_storage_client import BlobStorageClient
from src.routers.voice_model.language_entity import Language

from vall_e_x.app import make_npz_prompt, infer_from_prompt


class VoiceModelService:
    def create_model(
        self, user_id: str,create_voice_model_dto:CreateVoiceModelDto
    ):
        client = BlobStorageClient()
        dto=create_voice_model_dto
        audio_file_data = client.fetch_recorded_audio(dto.train_sound_file_name)
        bytes_io = io.BytesIO(audio_file_data)
        data = read(bytes_io)
        sr=data[1]
        wav=data[0]
        result = make_npz_prompt(user_id,sr, wav,dto.language.value)
        
        if result[1] is None:
            return None
        file_path = result[1]
        with open(file_path,'rb') as npz_file:
            npz_data= npz_file.read()
            client.upload_voice_model(f"{user_id}.npz",npz_data)
        print(file_path)
        os.remove(file_path)
        backend_domain=os.environ.get("AIRSHIP_ENDPOINT_URL")
        # httpx.post(f"{backend_domain}/v1/users/{user_id}/voice_model/status/done")

        del(client,dto,audio_file_data,bytes_io,data,sr,wav,result,file_path)

    def create_sound_from_model(
        self, user_id: str, create_voice_sound_dto:CreateVoiceSoundDto
    ):
        blob_storage_client=BlobStorageClient()
        npz_data=blob_storage_client.fetch_npz_prompt(f"{user_id}.npz")
        dto=create_voice_sound_dto
        npz_bytes= io.BytesIO(npz_data.readall())
        
        generate_result = infer_from_prompt(dto.content,dto.language.value,npz_bytes)
        if generate_result[1] is None:
            return None
        sr=generate_result[1][0]
        wav_pr=generate_result[1][1]
        
        audio_stream=io.BytesIO()
        audio_stream.name=dto.ar_assets_id
        
        write(audio_stream,wav_pr,sr,format= "WAV")
        audio_stream.seek(0)
        file_bytes = audio_stream.read()
        
        blob_storage_client.upload_voice_sound(f"{dto.ar_assets_id}.wav",file_bytes)

        backend_domain=os.environ.get("AIRSHIP_ENDPOINT_URL")
        # httpx.post(f"{backend_domain}/v1/users/ar_assets/{dto.ar_assets_id}/status/done")

        del(blob_storage_client,npz_data,npz_bytes,generate_result,sr,wav_pr,audio_stream,file_bytes)
