import pytest
import json

from src.assertions.global_assertions import assert_response_schema
from src.headers.headers import get_header_with_token1,get_header_with_tokenPlans
from config import BASE_URI,TOKEN
from src.common.logger import log_api_call
from src.common.static_data_modules import StaticDataModules
from src.common.static_data_plans import StaticDataPlans
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.assertions.asserts_attachment import assert_response_status_code_global
from src.resources.payloads.payloads_plans.payloads_plans import assert_request_plan_payload
from src.utils.api_calls import request_function
#Descripcion:  Crea un plan de manera correcta
#Prioridad: Alta
@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.regression
def test_DL_TC033_crear_un_plan(get_url,setup_delete_plan_by_id):
    payload = assert_request_plan_payload()
    assert_response_schema(payload, "plan_schema_request.json", "schema_plan_create")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.plan.value,
                                StaticDataPlans.default_url_suffix.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call("POST",get_url, get_header_with_tokenPlans(), payload, TOKEN, response)
    assert_response_status_code_global(200, response.status_code)
    assert_response_schema(response.json(), "plan_create_success_schema.json", "schema_plan_create")
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] is True
    setup_delete_plan_by_id(response.json()["result"]["id"])

#Descripcion: Crea un plan con descripcion devuelve codigo 200 de que se creo correctamente ya que no es un campo obligatorio
#Prioridad: Baja
@pytest.mark.positive
@pytest.mark.regression
def test_DL_TC034_crear_plan_con_descripcion(get_url, setup_delete_plan_by_id):
    payload = assert_request_plan_payload(description="Descripción del plan de prueba")
    assert_response_schema(payload, "plan_schema_request.json", "schema_plan_create")

    response = request_function(
        StaticDataVerbs.post.value,
        get_url,
        StaticDataModules.plan.value,
        StaticDataPlans.default_url_suffix.value,
        StaticDataHeaders.default_header.value,
        json.dumps(payload)
    )
    assert_response_status_code_global(200, response.status_code)
    assert_response_schema(response.json(), "plan_create_success_schema.json", "schema_plan_create")
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] is True
    setup_delete_plan_by_id(response.json()["result"]["id"])

#Descripcion: Crea un plan sin descripocion devuelve codigo 200 de que se creo correctamente ya que no es un campo obligatorio
#Prioridad:  Baja
@pytest.mark.regression
@pytest.mark.positive
def test_DL_TC035_crear_plan_sin_descripcion(get_url, setup_delete_plan_by_id):
    payload = assert_request_plan_payload(description=None)
    assert_response_schema(payload, "plan_schema_request.json", "schema_plan_create")
    response = request_function(
        StaticDataVerbs.post.value,
        get_url,
        StaticDataModules.plan.value,
        StaticDataPlans.default_url_suffix.value,
        StaticDataHeaders.default_header.value,
        json.dumps(payload)
    )
    assert_response_status_code_global(200, response.status_code)
    assert_response_schema(response.json(), "plan_create_success_schema.json", "schema_plan_create")
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] is True
    setup_delete_plan_by_id(response.json()["result"]["id"])

#Descripcion: Debuelve un error 401 al tratar de crear un plan si un token
#Prioridad: Alta
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC036_Crear_un_plan_sin_autenticación(get_url):
    payload = assert_request_plan_payload()
    assert_response_schema(payload, "plan_schema_request.json", "schema_plan_create")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataPlans.default_url_suffix.value, StaticDataHeaders.no_token_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "plan_error_401_noToken.json", "schema_plan_create")
    assert_response_status_code_global(401, response.status_code)

#Descripcion:  Debuelve un error 401 al intentar crear un plan con un token caducado
#Prioridad: Alta
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC037_Crear_un_plan_Con_token_caducado(get_url):
    payload = assert_request_plan_payload()
    assert_response_schema(payload, "plan_schema_request.json", "schema_plan_create")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.suite.value,
                                StaticDataPlans.default_url_suffix.value, StaticDataHeaders.invalid_token_header.value,
                                json.dumps(payload))

    log_api_call(method="POST",
                 url=response.url,
                 headers=response.headers,
                 payload=payload,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "plan_error_401_noToken.json", "schema_plan_create")
    assert_response_status_code_global(401, response.status_code)

#Descripcion: Debuelve un error 400 al sobrepasar el limite minimo del campo code
#Prioridad: Media
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC038_Verificar_el_límite_mínimo_de_caracteres_en_el_campo_code(get_url):
    payload = assert_request_plan_payload()
    assert_response_schema(payload, "plan_schema_request.json", "schema_plan_create")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.plan.value,
                                StaticDataPlans.lim_min_code.value,
                                StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call("POST",get_url, get_header_with_token1(), payload, TOKEN, response)
    assert_response_schema(response.json(), "plan_error_400.json", "schema_plan_create")
    assert_response_status_code_global(400, response.status_code)

#Descripcion: Debuelve un error 400 al verificar el limite maximo en el campo code
#Prioridad: Meda
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC039_Verificar_el_límite_maximo_de_caracteres_en_el_campo_code(get_url):
    payload = assert_request_plan_payload()
    assert_response_schema(payload, "plan_schema_request.json", "schema_plan_create")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.plan.value,
                                StaticDataPlans.lim_max_code.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call("POST",get_url, get_header_with_token1(), payload, TOKEN, response)
    assert_response_schema(response.json(), "plan_error_400.json", "schema_plan_create")
    assert_response_status_code_global(400, response.status_code)


#Descripcion: Debuelve un error 404 al colocar datos negativos en el campo code
#Prioridad: Media
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC040_Colocar_valores_negativos_en_el_campo_code(get_url):
    payload = assert_request_plan_payload()
    assert_response_schema(payload, "plan_schema_request.json", "schema_plan_create")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.plan.value,
                                StaticDataPlans.numeric_negative_code, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call("POST",get_url, get_header_with_token1(), payload, TOKEN, response)
    assert_response_schema(response.json(), "plan_error_404.json", "schema_plan_create")
    assert_response_status_code_global(404, response.status_code)

#Descripcion: Debuelve un error 404 al colocarcaracteres especiales en el campo code
#Prioridad: Media
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC041_Colocar_caracteres_especiales_en_el_campo_code(get_url):
    payload = assert_request_plan_payload()
    assert_response_schema(payload, "plan_schema_request.json", "schema_plan_create")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.plan.value,
                                StaticDataPlans.char_special_code, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call("POST", get_url, get_header_with_token1(), payload, TOKEN, response)
    assert_response_schema(response.json(), "plan_error_404.json", "schema_plan_create")
    assert_response_status_code_global(404, response.status_code)

#Descripcion: Debuelve un error 404 al colocar el caracter espacio"  " en el campo code
#Prioridad: Media
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC042_Colocar_solo_carácter_espacio_en_el_campo_code(get_url):
    payload = assert_request_plan_payload()
    assert_response_schema(payload, "plan_schema_request.json", "schema_plan_create")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.plan.value,
                                StaticDataPlans.char_space, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call("POST",get_url, get_header_with_token1(), payload, TOKEN, response)
    assert_response_schema(response.json(), "plan_error_404.json", "schema_plan_create")
    assert_response_status_code_global(404, response.status_code)

#Descripcion: Debuelve un error 404 al no colocar un codigo de poryecto en el campo code
#Prioridad: Alta
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC043_Crear_plan_sin_colocar_el_proyecto_en_el_campo_code(get_url):
    payload = assert_request_plan_payload()
    assert_response_schema(payload, "plan_schema_request.json", "schema_plan_create")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.plan.value,
                                StaticDataPlans.no_code, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call("POST",get_url, get_header_with_token1(), payload, TOKEN, response)
    assert_response_schema(response.json(), "plan_error_404.json", "schema_plan_create")
    assert_response_status_code_global(404, response.status_code)

#Descripcion: Debuelve un error 404 al colocar una url mal formada
#Prioridad: Media
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC044_Colocar_un_mal_formato_de_URL(get_url):
    payload = assert_request_plan_payload()
    assert_response_schema(payload, "plan_schema_request.json", "schema_plan_create")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.plan.value,
                                StaticDataPlans.no_code, StaticDataHeaders.default_header.value,
                                json.dumps(payload))

    log_api_call("POST",get_url, get_header_with_token1(), payload, TOKEN, response)
    assert_response_schema(response.json(), "plan_error_404.json", "schema_plan_create")
    assert_response_status_code_global(404, response.status_code)

#Descripcion: Debuelve un error 400 al sobrepasar el limite maximo de caracteres en el campo title
#Prioridad: Alta
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC045_Verificar_el_límite_máximo_de_caracteres_en_el_campo_title(get_url):
    payload = assert_request_plan_payload(title="A" * 300)
    assert_response_schema(payload, "plan_schema_request.json", "schema_plan_create")
    response = request_function(
        StaticDataVerbs.post.value,
        get_url,
        StaticDataModules.plan.value,
        StaticDataPlans.default_url_suffix.value,
        StaticDataHeaders.default_header.value,
        json.dumps(payload)
    )
    log_api_call("POST", get_url, get_header_with_token1(), payload, TOKEN, response)
    assert_response_schema(response.json(), "plan_error_400.json", "schema_plan_create")
    assert_response_status_code_global(400, response.status_code)

#Descripcion: Se puede crear un titulo con caracteres negativos
#Prioridad: Baja
@pytest.mark.regression
@pytest.mark.positive
def test_DL_TC046_title_valores_negativos(get_url,setup_delete_plan_by_id):
    payload = assert_request_plan_payload(title="-123")
    assert_response_schema(payload, "plan_schema_request.json", "schema_plan_create")
    response = request_function(
        StaticDataVerbs.post.value,
        get_url,
        StaticDataModules.plan.value,
        StaticDataPlans.default_url_suffix.value,
        StaticDataHeaders.default_header.value,
        json.dumps(payload)
    )
    log_api_call("POST", get_url, get_header_with_tokenPlans(), payload, TOKEN, response)
    assert_response_status_code_global(200, response.status_code)
    assert_response_schema(response.json(), "plan_create_success_schema.json", "schema_plan_create")
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] is True
    setup_delete_plan_by_id(response.json()["result"]["id"])

#Descripcion: Se puede crear un titulo con caracteres especiales
#Prioridad: Baja
@pytest.mark.regression
@pytest.mark.positive
def test_DL_TC047_title_caracteres_especiales(get_url,setup_delete_plan_by_id):
    payload = assert_request_plan_payload(title="@@@###")
    assert_response_schema(payload, "plan_schema_request.json", "schema_plan_create")
    response = request_function(
        StaticDataVerbs.post.value,
        get_url,
        StaticDataModules.plan.value,
        StaticDataPlans.default_url_suffix.value,
        StaticDataHeaders.default_header.value,
        json.dumps(payload)
    )
    log_api_call("POST", get_url, get_header_with_tokenPlans(), payload, TOKEN, response)
    assert_response_status_code_global(200, response.status_code)
    assert_response_schema(response.json(), "plan_create_success_schema.json", "schema_plan_create")
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] is True
    setup_delete_plan_by_id(response.json()["result"]["id"])

#Descripcion: Debuelve un error 400 al crear un titulo con el caracter espacio "   "
#Prioridad: Media
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC048_title_solo_espacios(get_url):
    payload = assert_request_plan_payload(title="   ")
    assert_response_schema(payload, "plan_schema_request.json", "schema_plan_create")
    response = request_function(
        StaticDataVerbs.post.value,
        get_url,
        StaticDataModules.plan.value,
        StaticDataPlans.default_url_suffix.value,
        StaticDataHeaders.default_header.value,
        json.dumps(payload)
    )
    log_api_call("POST", get_url, get_header_with_token1(), payload, TOKEN, response)
    assert_response_schema(response.json(), "plan_error_400.json", "schema_plan_create")
    assert_response_status_code_global(400, response.status_code)


#Descripcion: Debuelve un error 422 al colocar valores negativos en el campo cases
#Prioridad: Alta
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC049_cases_valores_negativos(get_url):
    payload = assert_request_plan_payload(cases=[-1])
    assert_response_schema(payload, "plan_schema_request.json", "schema_plan_create")
    response = request_function(
        StaticDataVerbs.post.value,
        get_url,
        StaticDataModules.plan.value,
        StaticDataPlans.default_url_suffix.value,
        StaticDataHeaders.default_header.value,
        json.dumps(payload)
    )
    log_api_call("POST", get_url, get_header_with_token1(), payload, TOKEN, response)
    assert_response_status_code_global(422, response.status_code)
    assert_response_schema(response.json(), "plan_error_422_cases.json", "schema_plan_create")

#Descripcion: Debuelve un error 400 al colocar caracteres especiales en el campo cases
#Prioridad: Media
@pytest.mark.regression
@pytest.mark.negative
def test_DL_TC050_cases_caracteres_especiales(get_url):
    payload = assert_request_plan_payload(cases=["@#!"])
    assert_response_schema(payload, "plan_create_success_test52.json", "schema_plan_create")
    response = request_function(
        StaticDataVerbs.post.value,
        get_url,
        StaticDataModules.plan.value,
        StaticDataPlans.default_url_suffix.value,
        StaticDataHeaders.default_header.value,
        json.dumps(payload)
    )
    log_api_call("POST", get_url, get_header_with_token1(), payload, TOKEN, response)
    assert_response_status_code_global(400, response.status_code)
    assert_response_schema(response.json(), "plan_error_400.json", "schema_plan_create")

#Descripcion: Debuelve un error 400 al colocar el caracter espacio "  " en el campo cases
#Prioridad:Media
@pytest.mark.regression
@pytest.mark.negative 
def test_DL_TC051_cases_solo_espacios(get_url):
    payload = assert_request_plan_payload(cases=["   "])
    assert_response_schema(payload, "plan_create_success_test52.json", "schema_plan_create")
    response = request_function(
        StaticDataVerbs.post.value,
        get_url,
        StaticDataModules.plan.value,
        StaticDataPlans.default_url_suffix.value,
        StaticDataHeaders.default_header.value,
        json.dumps(payload)
    )
    log_api_call("POST", get_url, get_header_with_token1(), payload, TOKEN, response)
    assert_response_status_code_global(400, response.status_code)
    assert_response_schema(response.json(), "plan_error_400.json", "schema_plan_create")
