import pytest
import json
from config import TOKEN,TOKEN_Invalido
import jsonschema
from src.resources.payloads.payloads_custom_field.payloads_get_custom_field import get_payload_by_id
from src.assertions.add_custom_field_assertions import assert_post_custom_field_request_schema,assert_post_custom_field_response_schema
from src.common.logger import log_api_call
from src.utils.load_resources import  assert_response_status_code
from src.common.static_data_modules import StaticDataModules
from src.common.static_data_custom_field import StaticDataCustomField
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.utils.api_calls import request_function

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_AE_TC001_crear_campo_personalizado_con_datos_validos(get_url,setup_delete_custom_field_by_id):

    payload = get_payload_by_id("AE_TC001")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc1")
    response = request_function(StaticDataVerbs.post.value,get_url, StaticDataModules.custom_field.value,StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,json.dumps(payload) )

    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    response_data = response.json()
    assert_post_custom_field_response_schema(response_data, "schema_salida_tc1")
    assert_response_status_code(response.status_code, 200)
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] == True
    setup_delete_custom_field_by_id(response.json()["result"]["id"])

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC002_Intentar_crear_un_campo_personalizado_sin_titulo(get_url):

    payload = get_payload_by_id("AE_TC002")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc02")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers= response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert_post_custom_field_response_schema(response.json(), "schema_salida_tc02")
    assert_response_status_code(response.status_code, 400)



@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC003_realizar_una_solicitud_sin_autenticacion(get_url):

    payload = get_payload_by_id("AE_TC003")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.invalid_token_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN_Invalido,
        response=response
    )
    assert response.status_code == 401
    assert_post_custom_field_response_schema(response.json(), "schema_salida_sin_authorization")
    assert_response_status_code(response.status_code, 401)


@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC004_enviar_valor_no_permitido_en_el_campo_type(get_url):

    payload = get_payload_by_id("AE_TC004")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert_post_custom_field_response_schema(response.json(), "schema_salida_sin_valores")
    assert_response_status_code(response.status_code, 400)


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_AE_TC005_verificar_campos_obligatorios_title_type_entity_de_campo_personalizado(get_url,setup_delete_custom_field_by_id):

    payload = get_payload_by_id("AE_TC005")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )

    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")
    assert_response_status_code(response.status_code, 200)
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] == True
    setup_delete_custom_field_by_id(response.json()["result"]["id"])


@pytest.mark.positive
@pytest.mark.regression
def test_AE_TC006_registrar_un_campo_personalizado_con_entity_case(get_url,setup_delete_custom_field_by_id):

    payload = get_payload_by_id("AE_TC006")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")
    assert_response_status_code(response.status_code, 200)
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] == True
    setup_delete_custom_field_by_id(response.json()["result"]["id"])


@pytest.mark.positive
@pytest.mark.regression
def test_AE_TC007_registrar_un_campo_personalizado_con_entity_run(get_url,setup_delete_custom_field_by_id):

    payload = get_payload_by_id("AE_TC007")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")
    assert_response_status_code(response.status_code, 200)
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] == True
    setup_delete_custom_field_by_id(response.json()["result"]["id"])

@pytest.mark.positive
@pytest.mark.regression
def test_AE_TC008_registrar_un_campo_personalizado_con_entity_defect(get_url,setup_delete_custom_field_by_id):

    payload = get_payload_by_id("AE_TC008")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")
    assert_response_status_code(response.status_code, 200)
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] == True
    setup_delete_custom_field_by_id(response.json()["result"]["id"])

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_AE_TC009_validar_que_el_campo_tipo_selectbox_requiere_valores_para_registrar(get_url,setup_delete_custom_field_by_id):

    payload = get_payload_by_id("AE_TC009")
    assert_post_custom_field_request_schema(payload, "schema_entrada_especial")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")
    assert_response_status_code(response.status_code, 200)
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] == True
    setup_delete_custom_field_by_id(response.json()["result"]["id"])
   


@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC010_crear_selectbox_sin_valores(get_url):

    payload = get_payload_by_id("AE_TC010")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )

    assert_post_custom_field_response_schema(response.json(), "schema_salida_especial")
    assert_response_status_code(response.status_code, 400)

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_AE_TC011_validar_que_el_campo_tipo_radio_requiere_valores_para_registrar(get_url,setup_delete_custom_field_by_id):

    payload = get_payload_by_id("AE_TC011")
    assert_post_custom_field_request_schema(payload, "schema_entrada_especial")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )

    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")
    assert_response_status_code(response.status_code, 200)
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] == True
    setup_delete_custom_field_by_id(response.json()["result"]["id"])

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC012_crear_radio_sin_valores(get_url):

    payload = get_payload_by_id("AE_TC012")
    assert_post_custom_field_request_schema(payload,"schema_entrada_tc")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )

    assert_post_custom_field_response_schema(response.json(), "schema_salida_especial")
    assert_response_status_code(response.status_code, 400)


@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_AE_TC013_validar_que_el_campo_tipo_multiselec_requiere_valores_para_registrar(get_url,setup_delete_custom_field_by_id):

    payload = get_payload_by_id("AE_TC013")
    assert_post_custom_field_request_schema(payload, "schema_entrada_especial")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )

    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")
    assert_response_status_code(response.status_code, 200)
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] == True
    setup_delete_custom_field_by_id(response.json()["result"]["id"])
    

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC014_crear_un_multiselect_sin_valores(get_url):

    payload = get_payload_by_id("AE_TC014")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )

    assert_post_custom_field_response_schema(response.json(), "schema_salida_sin_valores")
    assert_response_status_code(response.status_code, 400)
    



@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC015_enviar_valor_fuera_del_limite_inferior_de_type_numero_negativo(get_url):

    payload = get_payload_by_id("AE_TC015")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )

    assert_post_custom_field_response_schema(response.json(), "schema_salida_sin_valores")
    assert_response_status_code(response.status_code, 400)
    

@pytest.mark.positive
@pytest.mark.smoke
@pytest.mark.regression
def test_AE_TC016_Enviar_valor_minimo_permitido_en_type_0(get_url,setup_delete_custom_field_by_id):

    payload = get_payload_by_id("AE_TC016")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )



    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")
    assert_response_status_code(response.status_code, 200)
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] == True
    setup_delete_custom_field_by_id(response.json()["result"]["id"])



@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_AE_TC017_Enviar_valor_maximo_permitido_en_type_9(get_url,setup_delete_custom_field_by_id):

    payload = get_payload_by_id("AE_TC017")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )

    assert_post_custom_field_response_schema(response.json(), "schema_salida_correcto")
    assert_response_status_code(response.status_code, 200)
    assert response.json()["result"]["id"] is not None
    assert response.json()["status"] == True
    setup_delete_custom_field_by_id(response.json()["result"]["id"])


@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC018_Enviar_valor_fuera_del_limite_superior_de_type_10(get_url):

    payload = get_payload_by_id("AE_TC018")
    assert_post_custom_field_request_schema(payload, "schema_entrada_tc")
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )

    assert_post_custom_field_response_schema(response.json(), "schema_salida_sin_valores")
    assert_response_status_code(response.status_code, 400)




@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC019_Enviar_numero_decimal_negativo_como_valor_de_type(get_url):

    payload = get_payload_by_id("AE_TC019")
    with pytest.raises(jsonschema.exceptions.ValidationError):
         assert_post_custom_field_request_schema(payload, "schema_entrada_tc",expect_error=True)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )

    assert_post_custom_field_response_schema(response.json(), "schema_salida_decimal")
    assert_response_status_code(response.status_code, 400)



@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC020_Enviar_numero_decimal_positivo_valor_de_type(get_url):

    payload = get_payload_by_id("AE_TC020")
    with pytest.raises(jsonschema.exceptions.ValidationError):
        assert_post_custom_field_request_schema(payload, "schema_entrada_tc",expect_error=True)
    response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.valido_custom_post.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="POST",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )

    assert_post_custom_field_response_schema(response.json(), "schema_salida_decimal")
    assert_response_status_code(response.status_code, 400)
