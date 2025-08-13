import pytest

from config import TOKEN
from src.assertions.assert_suites import validate_path_params
from src.common.logger import log_api_call
from src.common.static_data_modules import StaticDataModules
from src.common.static_data_suites import StaticDataSuites
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.utils.api_calls import request_function
from src.utils.load_resources import assert_response_schema, assert_response_status_code_global


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_SM_TC038_Eliminar_un_conjunto_de_pruebas_con_un_ID_valido(get_url, setup_add_suite):
    """
    Descripción: Función para eliminar un conjunto de pruebas, con url, header, código e id válidos, para obtener
    resultado 200.
    """
    id_to_delete = setup_add_suite["result"]["id"]
    validate_path_params(id_to_delete, int)
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.suite.value,
                                f"{StaticDataSuites.default_url_suffix.value}/{id_to_delete}", StaticDataHeaders.default_header.value,
                                None)
    log_api_call(method="DELETE",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "add_suite_schema_response.json", "schema_suite")
    assert_response_status_code_global(200, response.status_code)
    assert response.json()["result"]["id"] == id_to_delete
    assert response.json()["status"] == True
    #assert response.headers == StaticDataHeaders.default_header.value