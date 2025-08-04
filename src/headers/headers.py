from config import TOKEN,TOKEN_inv


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
def get_header_with_token_inv():
    headers = {
        "accept": "application/json",
        "Token": f"{TOKEN_inv}"
    }
    return headers