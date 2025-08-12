import os
import sys

import pytest
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

