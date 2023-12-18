import os
from azure.storage.blob import BlobServiceClient,BlobClient
from src.utils.error.env import EnviomentLoadException
from src.utils.error.core import ResourceConflictException

voice_models_container_name = "voice-models"
voice_sounds_container_name = "voice-sounds"
train_sounds_container_name = "train-sounds"


class BlobStorageClient:
    client: BlobServiceClient

    def __init__(self) -> None:
        connect_str = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")
        if connect_str is None or connect_str is "":
            raise EnviomentLoadException()

        self.client = BlobServiceClient.from_connection_string(conn_str=connect_str)

    def is_exists_blob(self,blob_client:BlobClient)->bool:
        return blob_client.exists()
    
    def upload_voice_model(self, file_name: str, data: bytes):
        container_client = self.client.get_container_client(voice_models_container_name)
        is_exists = self.is_exists_blob(container_client.get_blob_client(file_name))
        if is_exists:
             container_client.delete_blob(file_name)
        container_client.upload_blob(file_name, data=data)

    def upload_voice_sound(self, file_name: str, data: bytes):
        container_client = self.client.get_container_client(voice_sounds_container_name)
        is_exists= self.is_exists_blob(container_client.get_blob_client(file_name))
        if is_exists:
            raise ResourceConflictException()
        container_client.upload_blob(file_name, data=data)

    def fetch_recorded_audio(self, file_name: str):
        container_client = self.client.get_container_client(train_sounds_container_name)
        blob_client = container_client.get_blob_client(file_name)
        blob =  blob_client.download_blob()
        file_bytes =  blob.readall()
        file_bytes.replace(b'\x00', b'')
        return file_bytes

    def fetch_npz_prompt(self, file_name: str):
        container_client = self.client.get_container_client(
            voice_models_container_name
        )
        blob_client = container_client.get_blob_client(file_name)
        npz_blob = blob_client.download_blob()
        # file_bytes = await npz_blob.readall()

        return npz_blob
