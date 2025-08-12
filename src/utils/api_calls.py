from importlib.metadata import files

import requests
from src.common.url import get_url_parametrized
from src.headers.headers import generate_headers


"""
Funcion para realizar una solicitud
"""

def request_function(method ,get_url, module, code = None, header_type = None, payload = None):
    url = get_url_parametrized(get_url, module, code)
    print(url)
    headers = generate_headers(header_type)
    response = requests.request(method, url, headers=headers, data=payload)
    return response

def request_function1(method ,get_url, module, code = None, header_type = None, payload = None,files=None):
    url = get_url_parametrized(get_url, module, code)
    print(url)
    headers = generate_headers(header_type)
    response = requests.request(method, url, headers=headers, data=payload,files=files)
    return response