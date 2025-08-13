import os
import sys
import random
import pytest
import json
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from config import *
from src.common.static_data_custom_field import StaticDataCustomField
from src.common.static_data_modules import StaticDataModules
from src.common.static_data_suites import StaticDataSuites
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.headers.headers import *
from src.utils.api_calls import request_function
from src.resources.payloads.payloads_case.payloads_post_case import assert_request_payload, name_random_cases

@pytest.fixture(scope='session')
def get_url():
    return BASE_URI

@pytest.fixture(scope='session')
def get_invalid_url():
    return BASE_INVALID_URI

@pytest.fixture(scope='session')
def get_token():
    return TOKEN


"""
Tierdown para eliminar suite
"""
@pytest.fixture(scope="function")
def setup_delete_suite_by_id(get_url):
    suite_id_to_delete = None
    def registrar_id(suite_id):
        nonlocal suite_id_to_delete
        suite_id_to_delete = suite_id

    yield registrar_id
    if suite_id_to_delete:
        response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.suite.value,
                                    f"{StaticDataSuites.default_url_suffix.value}/{suite_id_to_delete}",StaticDataHeaders.default_header.value)
        assert response.status_code == 200


@pytest.fixture(scope="function")
def setup_delete_custom_field_by_id(get_url):
    custom_field_id_to_delete = None
    def registrar_id(custom_field_id):
        nonlocal custom_field_id_to_delete
        custom_field_id_to_delete = custom_field_id

    yield registrar_id
    if custom_field_id_to_delete:
        response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.custom_field.value,
                                    f"{StaticDataCustomField.delete_custom_field1.value}/{custom_field_id_to_delete}",StaticDataHeaders.default_header.value)
        assert response.status_code == 200

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
        delete_case_created(cid,base_url)

@pytest.fixture(scope="function")
def patch_add_case(get_url):
    request = assert_request_payload(name_random_cases(), random.choice([2, 3, 4, 5]), random.choice([1, 2, 3]),
                                     random.choice([2, 3, 8]), random.choice([0, 1, 2]), random.choice([0, 2]))
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,
                                StaticDataSuites.default_url_suffix.value,
                                header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request))
    id_case = response.json()["result"]["id"]
    yield response.json()
    delete_case_created(id_case,get_url)

def delete_case_created(id_case,get_url):
    base_url = get_url
    try:
        resp = request_function(StaticDataVerbs.delete.value, base_url, StaticDataModules.case.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id_case}",
                                StaticDataHeaders.default_header.value)
        if resp.status_code not in (200, 204, 404):
            print(f"[post_resource_single teardown] warning: delete {id_case} devolvió {resp.status_code}")
    except Exception as e:
        print(f"[post_resource_single teardown] error al eliminar {id_case}: {e}")