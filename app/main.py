import os
import fastapi
import uvicorn
from src.app_container import AppContainer
from dotenv import load_dotenv
from firebase_admin import initialize_app, credentials

load_dotenv()

cred = credentials.Certificate(os.environ["FIREBASE_ADMIN_TOKEN"])
initialize_app(cred)

app = fastapi.FastAPI()
app_container = AppContainer()
app.include_router(app_container.get_router())
app_container.include_routers(app.include_router)


if __name__ =="__main__":
    uvicorn.run(app=app,host="0.0.0.0",port=8000)