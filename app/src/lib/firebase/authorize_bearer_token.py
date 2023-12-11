from firebase_admin.auth import (
    verify_id_token,
    InvalidIdTokenError,
    ExpiredIdTokenError,
)


def authorize_bearer_token(token: str) -> bool:
    found_bearer_str_index = token.find("Bearer ")
    if found_bearer_str_index == -1 or found_bearer_str_index != 0:
        return False
    token_body = token.replace("Bearer ", "")
    try:
        verify_id_token(token_body)

    except (
        ValueError,
        InvalidIdTokenError,
        ExpiredIdTokenError,
    ) as e:
        match e.default_message:
            case str():
                print(e.default_message)
            case _:
                print("message type unknown")
        return False
    return True
