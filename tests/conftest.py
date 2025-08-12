import pytest
import requests
from config import *
from src.headers.headers import *
from src.common.static_headers import StaticDataHeaders
from src.common.static_data_suites import StaticDataSuites
from src.common.static_data_modules import StaticDataModules
from src.common.static_verbs import StaticDataVerbs
from src.utils.api_calls import request_function

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
def post_resource_case(get_url):
    base_url = get_url
    client = {
        "created_id": None,  # aqui guardará el test el id creado
    }

    yield client

    # TEARDOWN: eliminar si existe
    cid = client.get("created_id")
    if cid:
        try:
            resp = request_function(StaticDataVerbs.delete.value,base_url,StaticDataModules.case.value,f"{StaticDataSuites.default_url_suffix.value}/{cid}",StaticDataHeaders.default_header.value)
            if resp.status_code not in (200, 204, 404):
                print(f"[post_resource_single teardown] warning: delete {cid} devolvió {resp.status_code}")
        except Exception as e:
            print(f"[post_resource_single teardown] error al eliminar {cid}: {e}")


