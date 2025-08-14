import json
import pytest

from config import TOKEN
from src.common.logger import log_api_call
from src.common.static_data_modules import StaticDataModules
from src.common.static_data_project import StaticDataProject
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.resources.payloads.payloads_project.payloads_project import create_request_project_payload, \
    create_request_project_payload_modificado, \
    create_request_project_payload_Sin_title, create_request_project_payload_Sin_descripcion, \
    create_request_project_payload_super_modified
from src.utils.api_calls import request_function
from src.utils.load_resources import assert_response_schema, assert_response_status_code_global


#Alta
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC001_Crear_un_proyecto_exitoso(get_url, get_token, setup_delete_project_by_code):
    payload = create_request_project_payload_super_modified()
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "add_project_schema_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)
    assert response.json()["result"]["code"] is not None
    assert response.json()["status"] == True
    setup_delete_project_by_code(response.json()["result"]["code"])


#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC002_Verificar_que_de_error_al_enviar_una_URL_mal_formada(get_invalid_url, get_token):
    payload = create_request_project_payload_super_modified()
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_invalid_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.invalid_token_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "post_error404_project_response.json", "schemas_project")
    assert_response_status_code_global(404, response.status_code)

#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC003_Verificar_que_de_error_Crear_proyecto_con_nombre_existente_en_lista(get_url):
    #refactorizar mas
    payload = create_request_project_payload_super_modified()
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,
                                StaticDataProject.valid_project_default .value, StaticDataHeaders.no_content_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(400, response.status_code)

#Media
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC004_Verificar_que_no_permita_crear_un_proyecto_con_un_body_inválido(get_url):
    payload = create_request_project_payload_super_modified()
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,
                                StaticDataProject.valid_project_default .value, StaticDataHeaders.no_content_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(400, response.status_code)


#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC005_Verificar_que_no_permita_crear_un_proyecto_con_un_token_incorrecto(get_url, get_token):
    payload = create_request_project_payload_super_modified()
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.invalid_token_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "post_error401_project_response.json", "schemas_project")
    assert_response_status_code_global(401, response.status_code)



#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC006_Verificar_que_no_permita_crear_un_proyecto_sin_autentificar(get_url, get_token):
    payload = create_request_project_payload_super_modified()
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.no_token_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "post_error401_project_response.json", "schemas_project")
    assert_response_status_code_global(401, response.status_code)



#Media
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_GCTC007_Crear_proyecto_con_todos_los_campos_disponibles(get_url, get_token, setup_delete_project_by_code):
    #Aumentar un campo en el payload
    payload = create_request_project_payload_super_modified()
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "add_project_schema_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)
    assert response.json()["result"]["code"] is not None
    assert response.json()["status"] == True
    setup_delete_project_by_code(response.json()["result"]["code"])


#Media
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC008_Verificar_crear_proyecto_sin_description(get_url, get_token, setup_delete_project_by_code):
    payload = create_request_project_payload_Sin_descripcion()
    assert_response_schema(payload, "add_proyect_schema_request_sin_descrip.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "add_project_schema_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)
    assert response.json()["result"]["code"] is not None
    assert response.json()["status"] == True
    setup_delete_project_by_code(response.json()["result"]["code"])


#Baja
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC009_Crear_proyecto_con_code_mayusculas(get_url, get_token, setup_delete_project_by_code):
    payload = create_request_project_payload_super_modified()
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "add_project_schema_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)
    assert response.json()["result"]["code"] is not None
    assert response.json()["status"] == True
    setup_delete_project_by_code(response.json()["result"]["code"])


#Alto
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC010_Crear_proyecto_con_code_numerico(get_url):
    payload = create_request_project_payload_super_modified(code="123789")
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(400, response.status_code)


#alta
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC011_Crear_proyecto_sin_title(get_url):
    payload = create_request_project_payload_Sin_title()
    assert_response_schema(payload, "add_project_schema_request_sin_title.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(400, response.status_code)


#Media
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC012_Crear_proyecto_con_code_caracteres_especiales(get_url):
    payload = create_request_project_payload_super_modified(code="@#$%#")
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(400, response.status_code)


#Media
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC013_Crear_proyecto_title_1_caracter_valido(get_url, get_token, setup_delete_project_by_code):
    payload = create_request_project_payload_super_modified(title=1)
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "add_project_schema_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)
    assert response.json()["result"]["code"] is not None
    assert response.json()["status"] == True
    setup_delete_project_by_code(response.json()["result"]["code"])


#Media
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC014_Crear_proyecto_title_2_caracteres_valido(get_url, get_token, setup_delete_project_by_code):
    payload = create_request_project_payload_super_modified(title=2)
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "add_project_schema_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)
    assert response.json()["result"]["code"] is not None
    assert response.json()["status"] == True
    setup_delete_project_by_code(response.json()["result"]["code"])


#Media
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC015_Crear_proyecto_title_224_caracteres_valido(get_url, get_token, setup_delete_project_by_code):
    payload = create_request_project_payload_super_modified(title=224)
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "add_project_schema_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)
    assert response.json()["result"]["code"] is not None
    assert response.json()["status"] == True
    setup_delete_project_by_code(response.json()["result"]["code"])


#Media
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC016_Crear_proyecto_title_225_caracteres_valido(get_url, get_token, setup_delete_project_by_code):
    payload = create_request_project_payload_super_modified(title=225)
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "add_project_schema_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)
    assert response.json()["result"]["code"] is not None
    assert response.json()["status"] == True
    setup_delete_project_by_code(response.json()["result"]["code"])


#Medio
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC017_Crear_proyecto_title_vacio_invalido(get_url):
    payload = create_request_project_payload_super_modified(title="")
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(400, response.status_code)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC018_Crear_proyecto_title_256_caracteres_invalido(get_url):
    payload = create_request_project_payload_super_modified(title=256)
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(400, response.status_code)


#Media
@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.regression
def test_GCTC019_Crear_proyecto_code_2_caracteres_valido(get_url, get_token, setup_delete_project_by_code):
    payload = create_request_project_payload_super_modified(code=2)
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "add_project_schema_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)
    assert response.json()["result"]["code"] is not None
    assert response.json()["status"] == True
    setup_delete_project_by_code(response.json()["result"]["code"])


#Media
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC020_Crear_proyecto_code_5_caracteres_valido(get_url, get_token, setup_delete_project_by_code):
    payload = create_request_project_payload_super_modified(code=5)
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "add_project_schema_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)
    assert response.json()["result"]["code"] is not None
    assert response.json()["status"] == True
    setup_delete_project_by_code(response.json()["result"]["code"])


#Media
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_GCTC021_Crear_proyecto_code_10_caracteres_valido(get_url, get_token, setup_delete_project_by_code):
    payload = create_request_project_payload_super_modified(code=10)
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "add_project_schema_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)
    assert response.json()["result"]["code"] is not None
    assert response.json()["status"] == True
    setup_delete_project_by_code(response.json()["result"]["code"])


#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC022_Crear_proyecto_code_vacio_invalido(get_url):
    payload = create_request_project_payload_super_modified(code="")
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(400, response.status_code)


#Alta
@pytest.mark.negative
@pytest.mark.regression
def test_GCTC023_Crear_proyecto_code_15_caracteres_invalido(get_url):
    payload = create_request_project_payload_super_modified(code=15)
    assert_response_schema(payload, "add_project_schema_request.json", "schemas_project")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,StaticDataProject.valid_project_default.value, StaticDataHeaders.default_header.value, json.dumps(payload))
    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_status_code_global(400, response.status_code)
