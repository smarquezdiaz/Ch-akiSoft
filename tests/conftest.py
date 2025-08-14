import json
import os
import sys
import random
from hmac import compare_digest

import pytest

from src.common.logger import log_api_call
from src.common.static_data_project import StaticDataProject
from src.resources.payloads.payloads_project.payloads_project import create_request_project_payload, \
    create_request_project_payload_super_modified
from src.utils.load_resources import assert_response_schema, assert_response_status_code_global

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from config import *
from src.common.static_data_custom_field import StaticDataCustomField
from src.common.static_data_modules import StaticDataModules
from src.common.static_data_suites import StaticDataSuites
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.common.static_data_plans import StaticDataPlans
from src.headers.headers import *
from src.utils.api_calls import request_function
from src.resources.payloads.payloads_case.payloads_post_case import *
from src.common.logger import log_api_call
from src.resources.payloads.payloads_suite.payloads_suite import create_request_suite_payload, \
    create_destination_id_payload
from src.utils.load_resources import assert_response_schema, assert_response_status_code_global
from src.resources.payloads.payloads_case.payloads_post_case import *

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
    request = case_request_payload(name_random_cases(), random_severity_case(), random_priority_case(),
                                   random_type_case(), random_status_case(), random_automation_case())
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

@pytest.fixture(scope="function")
def setup_delete_plan_by_id(get_url):
    plan_id_to_delete = None

    def registrar_id(plan_id):
        nonlocal plan_id_to_delete
        plan_id_to_delete = plan_id

    yield registrar_id

    if plan_id_to_delete:
        response = request_function(
            StaticDataVerbs.delete.value,
            get_url,
             StaticDataModules.plan.value,
            f"{StaticDataPlans.default_url_suffix.value}/{plan_id_to_delete}",
            StaticDataHeaders.default_header.value
        )
        assert response.status_code == 200

@pytest.fixture(scope="function")
def setup_delete_project_by_code(get_url):
    project_code_to_delete = None
    def registrar_code(project_code):
        nonlocal project_code_to_delete
        project_code_to_delete = project_code

    yield registrar_code
    if project_code_to_delete:
        response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                    f"{StaticDataProject.valid_project_default.value}/{project_code_to_delete}",StaticDataHeaders.default_header.value)
        assert response.status_code == 200


"""
Setup para agregar proyect
"""


def _add_project(get_url, **kwargs):
    payload = create_request_project_payload_super_modified(**kwargs)

    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")

    response = request_function(
        StaticDataVerbs.post.value,
        get_url,
        StaticDataModules.project.value,
        StaticDataProject.valid_project_default.value,
        StaticDataHeaders.default_header.value,
        json.dumps(payload)
    )

    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )

    assert_response_schema(response.json(), "add_project_schema_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)

    return response.json()


@pytest.fixture(scope="function")
def setup_add_project(get_url):
    return _add_project(get_url)


@pytest.fixture(scope="function")
def setup_add_project_2_character(get_url):
    return _add_project(get_url, code=2)

@pytest.fixture(scope="function")
def setup_add_project_10_character(get_url):
    return _add_project(get_url, code=10)

@pytest.fixture(scope="function")
def setup_add_project_minus(get_url):
    return _add_project(get_url, code="casa")
"""
Setup para agregar suite
"""
@pytest.fixture(scope="function")
def setup_add_suite(get_url):
    payload = create_request_suite_payload()
    assert_response_schema(payload, "add_suite_schema_request.json", "schema_suite")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suffix.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(200, response.status_code)
    return response.json()

"""
Setup para crear suite y devolver destination_id
"""
@pytest.fixture(scope="function")
def setup_add_suite_for_destination_id(setup_add_suite):
    destination_id = setup_add_suite["result"]["id"]
    payload = create_destination_id_payload(destination_id)
    return payload

"""
Tierdown para obtener y eliminar suite
"""
@pytest.fixture(scope="function")
def setup_get_and_delete_suite_by_id(get_url):
    suite_id_to_delete = None
    def registrar_id(suite_id):
        get_suite_by_id(get_url, suite_id)
        nonlocal suite_id_to_delete
        suite_id_to_delete = suite_id

    yield registrar_id
    if suite_id_to_delete:
        response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.suite.value,
                                    f"{StaticDataSuites.default_url_suffix.value}/{suite_id_to_delete}",StaticDataHeaders.default_header.value)
        assert response.status_code == 200

def get_suite_by_id(get_url,suite_id):
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{suite_id}",
                                StaticDataHeaders.default_header.value)
    assert response.status_code == 200