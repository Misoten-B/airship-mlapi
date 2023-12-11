from firebase_admin.auth import (
    verify_id_token,
    InvalidIdTokenError,
    ExpiredIdTokenError,
)


def authorize_bearer_token(token: str) -> bool:
    try:
        verify_id_token(token)

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
