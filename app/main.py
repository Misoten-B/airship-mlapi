import os
import fastapi
import uvicorn
from src.app_container import AppContainer
from dotenv import load_dotenv
from firebase_admin import initialize_app, credentials
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()

cred = credentials.Certificate(os.environ["FIREBASE_ADMIN_TOKEN"])
initialize_app(cred)

origins=[
    os.environ["AIRSHIP_ENDPOINT_URL"],
    "http://localhost:8080",
    ]

app = fastapi.FastAPI(docs_url="/api",openapi_url="/api/json")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )


app_container = AppContainer()
app.include_router(app_container.get_router())
app_container.include_routers(app.include_router)


if __name__ =="__main__":
    uvicorn.run(
        app=app,host="0.0.0.0",
        port=80,
        ssl_keyfile="/home/docker/vall_e_x_api/key.pem",
        ssl_certfile="/home/docker/vall_e_x_api/cert.pem"
        )
