from config import TOKEN,TOKEN_inv


def get_header_with_token():
    headers = {
        "accept": "application/json",
        "Token": f"{TOKEN}",
        'content-type': 'application/json'
    }
    return headers

def get_header_without_token():
    headers = {
        "accept": "application/json",
        'content-type': 'application/json'
    }
    return headers

def get_header_without_accept():
    headers = {
        "Token": f"{TOKEN}",
        'content-type': 'application/json'
    }
    return headers

def get_header_without_content():
    headers = {
        "accept": "application/json",
        "Token": f"{TOKEN}"
    }
    return headers
def get_header_with_token_inv():
    headers = {
        "accept": "application/json",
        "Token": f"{TOKEN_inv}"
    }
    return headers