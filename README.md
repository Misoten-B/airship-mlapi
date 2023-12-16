# Airship ML API

### Local Server URL
- http://localhost:8000
### Swagger
- http://localhost:8000/api
### Open API Schema Json
- http://localhost:8000/api/json

## Getting Start

1. Download Project And Large Files

    Download this project files from this repository and epoch-10.pt from https://huggingface.co/spaces/Plachta/VALL-E-X/resolve/main/epoch-10.pt
    
    please put epoch-10.pt app/vall_e_x and envioment files app

2. Building Docker image

    `docker compose build`

3. Creating Docker container

    `docker compose up -d`

4. Start Running Server
    
    `docker exec -it -u docker airship-mlapi-app-1 python3.11 main.py`

# How To Use

- ### Package Install

    `python3.11 -m pip install --user -r ~/vall_e_x_api/requirements.txt`

- ### Run Server
    `python3.11 main.py`