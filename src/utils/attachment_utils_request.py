import pytest
import requests
from config import BASE_URI, TOKEN
from src.headers.headers import get_header_with_token1, get_header_with_invalid_token
from src.common.logger import log_api_call
from src.assertions.asserts_attachment import assert_response_status_code_global
from src.utils.load_resources import assert_response_schema
from src.utils.getHash import obtener_hash_archivo

def delete_request(url: str, headers=None, token_override=None):
    #Envía una petición DELETE
    headers = headers or {}
    response = requests.delete(url, headers=headers)
    return response

def get_request(url: str, headers=None, token_override=None):
    #Envía una petición GET y registra el log de la llamada.
    headers = headers or {}
    response = requests.get(url, headers=headers)
    return response

def build_attachment_url(hash_value: str) -> str:
   # Construye la URL
    hash_value = hash_value.strip() if hash_value else ""
    if hash_value:
        return f"{BASE_URI}/attachment/{hash_value}"
    return f"{BASE_URI}/attachment/"

def build_invalid_url() -> str:
    #Devuelve una URL mal formada
    return f"{BASE_URI}/attac#hment//hash//"
