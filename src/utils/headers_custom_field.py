from config import TOKEN, TOKEN_Invalido

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
