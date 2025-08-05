from config import TOKEN, TOKEN_Invalido
from config import BASE_URI,TOKEN
def get_headers(token=None, invalido=False):
    if invalido:
        token = TOKEN_Invalido
    elif token is None:
        token = TOKEN

    return {
        'Token': token,
        'accept': 'application/json',
        'content-type': 'application/json'
    }
def custom_field_url(BASE_URI, field_id):
    return f"{BASE_URI}/custom_field/{field_id}"