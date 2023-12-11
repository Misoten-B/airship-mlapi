import os
from azure.storage.blob.aio import BlobServiceClient
from utils.error.env import EnviomentLoadException

voice_models_container_name = "voice-models"
voice_sounds_container_name = "audios"


class BlobStorageClient:
    client: BlobServiceClient

    def __init__(self) -> None:
        connect_str = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")
        if connect_str is None or connect_str is "":
            raise EnviomentLoadException()

        self.client = BlobServiceClient.from_connection_string(conn_str=connect_str)

    async def upload_voice_model(self, file_name: str, data: bytes | str):
        container_client = self.client.get_container_client(voice_models_container_name)
        await container_client.upload_blob(file_name, data=data)

    async def upload_voice_sound(self, file_name: str, data: bytes | str):
        container_client = self.client.get_container_client(voice_sounds_container_name)
        await container_client.upload_blob(file_name, data=data)
