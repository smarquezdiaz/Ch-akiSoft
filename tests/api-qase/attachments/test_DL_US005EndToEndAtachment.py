import io
import pytest
from config import BASE_URI, TOKEN
from src.assertions.global_assertions import assert_response_schema
from src.headers.headers import get_header_with_token1
from src.common.logger import log_api_call
from src.assertions.asserts_attachment import assert_response_status_code_global
from src.utils.attachment_utils_request import build_attachment_url, get_request, delete_request
from src.utils.getHash import obtener_hash_archivo
import requests
@pytest.mark.e2e
@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.regression
def test_DL_E2E_gestion_completa_archivo():
    #Obtener lista inicial
    url_list = f"{BASE_URI}/attachment"
    response_list = get_request(url_list, headers=get_header_with_token1())
    log_api_call("GET", response_list.url, get_header_with_token1(), None, TOKEN, response_list)
    assert_response_status_code_global(200, response_list.status_code)
    assert_response_schema(response_list.json(), "attachment_list_success_schema.json", "schema_attachment")

    #Subir archivo y obtener hash
    hash_archivo = obtener_hash_archivo(file_name="Hola Mundo +100.txt",
                                        file_content="Archivo de prueba generado para flujo E2E")

    #Verificar que el archivo este
    url_get_uploaded = build_attachment_url(hash_archivo)
    response_get_uploaded = get_request(url_get_uploaded, headers=get_header_with_token1())
    log_api_call("GET", response_get_uploaded.url, get_header_with_token1(), None, TOKEN, response_get_uploaded)
    assert_response_status_code_global(200, response_get_uploaded.status_code)

    #Eliminar archivo
    response_delete = delete_request(url_get_uploaded, headers=get_header_with_token1())
    log_api_call("DELETE", response_delete.url, get_header_with_token1(), None, TOKEN, response_delete)
    assert_response_status_code_global(200, response_delete.status_code)
    assert_response_schema(response_delete.json(), "attachment_delete_200.json", "schema_attachment")

    #Verificar que el archivo ya no exista
    response_get_deleted = get_request(url_get_uploaded, headers=get_header_with_token1())
    log_api_call("GET", response_get_deleted.url, get_header_with_token1(), None, TOKEN, response_get_deleted)
    assert_response_status_code_global(404, response_get_deleted.status_code)