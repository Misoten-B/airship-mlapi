# Airship ML API

### Local Server URL
- http://localhost:8000
### Open API
- http://localhost:8000/docs

## Getting Start

1. Building Docker image

    `docker compose build`

2. Creating Docker container

    `docker compose up -d`

3. Start Running Server
    
    `docker exec -it -u docker airship-mlapi-app-1 python3.11 main.py`

# How To Use

- ### Package Install

    `python3.11 -m pip install -r ~/workspace/requirements.txt`

- ### Run Server
    `python3.11 main.py`