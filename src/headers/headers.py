from config import TOKEN, TOKEN_Invalido


def generate_headers(header_type):
    match header_type:
        case "default_header":
            return get_header_with_token()
        case "no_content_header":
            return get_header_without_content()
        case "no_token_header":
            return get_header_without_token()
        case "no_accept_header":
            return get_header_without_accept()
        case "invalid_token_header":
            return get_header_with_invalid_token()
        case _:
            return get_header_with_token()


def get_header_with_token():
    headers = {
        "accept": "application/json",
        "Token": f"{TOKEN}",
        'content-type': 'application/json'
    }
    return headers
def get_header_with_token1():
    headers = {
        "accept": "application/json",
        "Token": f"{TOKEN}",
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

def get_header_with_invalid_token():
    headers = {
        "accept": "application/json",
        "Token": f"{TOKEN_Invalido}"
    }
    return headers
def get_header_with_tokenPlans():
    headers = {
        "accept": "application/json",
        'content-type': 'application/json',
        "Token": f"{TOKEN}"
    }
    return headers