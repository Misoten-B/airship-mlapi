from fastapi import HTTPException

from src.lib.firebase.auth import verify_id_token


def verify_bearer_token(token: str) -> bool:
    found_bearer_str_index = token.find("Bearer ")
    if found_bearer_str_index == -1 or found_bearer_str_index != 0:
        return False
    token_body = token.replace("Bearer ", "")
    return verify_id_token(token_body)
