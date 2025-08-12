import random
import string

def assert_request_project_payload(
    title: str | int | None = None,
    code: str | int | None = None,
    description: str | int | None = None,
) -> dict:
    payload = {
        "title": get_random_title() if title is None else str(title),
        "code": get_random_code() if code is None else str(code),
        "description": get_random_code() if description is None else str(description),
    }
    return payload

def get_random_title():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

def get_random_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))
