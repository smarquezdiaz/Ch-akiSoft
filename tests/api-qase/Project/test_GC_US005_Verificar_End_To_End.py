import json

import pytest

from src.common.static_data_modules import StaticDataModules
from src.common.static_data_project import StaticDataProject
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.resources.payloads.payloads_project.payloads_project import create_request_project_payload_super_modified
from src.utils.api_calls import request_function
from src.assertions.global_assertions import assert_response_status_code_global


#Alta
@pytest.mark.flujo
def test_GCTC001_Obtener_un_flujo_de_project(get_url):
        """
        Descripción: Verificar que el todo el flujp de crear, obtener y eliminar un proyecto se lleve de manera correcta y secuencial
        """
        payload = create_request_project_payload_super_modified()
        response_post = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,
                                    StaticDataProject.valid_project_default.value,
                                    StaticDataHeaders.default_header.value, json.dumps(payload))
        id_to_get = response_post.json()["result"]["code"]
        response_get = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,
                                        f"/{id_to_get}", StaticDataHeaders.default_header.value)
        id_to_delete = response_get.json()["result"]["code"]
        response_delete = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                           f"/{id_to_delete}",StaticDataHeaders.default_header.value)
        assert_response_status_code_global(200, response_delete.status_code)
