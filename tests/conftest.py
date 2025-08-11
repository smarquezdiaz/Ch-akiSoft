import pytest
import requests
from config import *
from src.headers.headers import *

@pytest.fixture(scope='session')
def get_url():
    return BASE_URI

@pytest.fixture(scope='session')
def get_invalid_url():
    return BASE_INVALID_URI

@pytest.fixture(scope='session')
def get_token():
    return TOKEN

@pytest.fixture(scope="function")
def post_resource_case(get_url, get_token):
    base_url = get_url
    headers = {
        "Token": get_token,
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    client = {
        "base_url": base_url,
        "headers": headers,
        "created_id": None,  # allí guardará el test el id creado
    }

    yield client

    # TEARDOWN: eliminar si created_id existe
    cid = client.get("created_id")
    if cid:
        try:
            delete_url = f"{base_url}/case/DEMO/{cid}"   # ajusta si tu API borra con otra ruta
            resp = requests.delete(delete_url, headers=headers, timeout=10)
            if resp.status_code not in (200, 204, 404):
                print(f"[post_resource_single teardown] warning: delete {cid} devolvió {resp.status_code}")
        except Exception as e:
            print(f"[post_resource_single teardown] error al eliminar {cid}: {e}")


