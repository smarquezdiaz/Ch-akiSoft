import pytest
import requests
import json
import jsonschema

from src.common.static_data_modules import StaticDataModules
from src.common.static_data_suites import StaticDataSuites
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.resources.payloads.payloads_suite.payloads_suite import create_request_suite_payload
from src.utils.api_calls import request_function


#Alta
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
@pytest.mark.e2e.Suite
def test_SM_TC079_Suite(get_url):
    """
    Descripción: Función para realizar un CRUD, crear, actualizar, obtener y eliminar un conjunto de pruebas
    resultado 200.
    """
    payload = create_request_suite_payload()
    response_post = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataSuites.default_url_suffix.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    id_to_update = response_post.json()["result"]["id"]
    payload = create_request_suite_payload()
    response_update = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id_to_update}",
                                StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    id_to_get = response_update.json()["result"]["id"]
    response_get = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id_to_get}",
                                    StaticDataHeaders.default_header.value)
    id_to_delete = response_get.json()["result"]["id"]
    response_delete= request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.suite.value,
                                    f"{StaticDataSuites.default_url_suffix.value}/{id_to_delete}",
                                    StaticDataHeaders.default_header.value)
    assert response_delete.status_code == 200