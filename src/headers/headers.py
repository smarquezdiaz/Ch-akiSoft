from config import TOKEN


def get_header_with_token():
    headers = {
        "accept": "application/json",
        "Token": f"{TOKEN}"
    }
    return headers

def get_header_without_token():
    headers = {
        "accept": "application/json",
    }
    return headers