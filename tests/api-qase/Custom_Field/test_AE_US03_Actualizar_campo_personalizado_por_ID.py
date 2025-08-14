import pytest
import json
from config import TOKEN,TOKEN_Invalido
from src.assertions.get_custom_field_assertions import assert_response_status_code_custom_field
from src.assertions.patch_custom_field_assertions import assert_patch_custom_field_request_schema,assert_patch_custom_field_response_schema
from src.common.logger import log_api_call
from src.common.static_data_custom_field import StaticDataCustomField
from src.common.static_data_modules import StaticDataModules
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.resources.payloads.payloads_custom_field.payloads_custom_field import get_payload_by_id
from src.utils.api_calls import request_function

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_AE_TC030_Actualizar_campo_personalizado_con_datos_validos(get_url):
    """Descripcion actualizar un campo personalizado existente"""
    payload = get_payload_by_id("AE_TC030")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_valida")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.patch_custom_field.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="PATCH",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_valida")
    assert_response_status_code_custom_field(response.status_code, 200)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC031_Actualizar_campo_personalizado_con_titulo_vacio(get_url):
    """Descripcion el usuario no podra actualizar  un campo personalizado si no pone titulo"""
    payload = get_payload_by_id("AE_TC031")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_valida")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.patch_custom_field1.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="PATCH",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_error_fields_status")
    assert_response_status_code_custom_field(response.status_code, 400)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC032_Actualizar_campo_personalizado_con_titulo_que_excede_255_caracteres(get_url):
    """Descripcion el usuario no podra actualizar  un campo personalizado si excede en caracteres del titulo"""

    payload = get_payload_by_id("AE_TC032")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_valida")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.patch_custom_field2.value, StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="PATCH",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data,"schema_salida_error_fields_status")
    assert_response_status_code_custom_field(response.status_code,400)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC033_Actualizar_campo_personalizado_con_ID_no_numerico_letras(get_url):
    """Descripcion el usuario no podra actualizar  un campo personalizado si ponemos letras en el id del campo que buscamos actualizar """

    payload = get_payload_by_id("title")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_valida")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                    StaticDataCustomField.patch_custom_field_letras.value,
                                    StaticDataHeaders.default_header.value,
                                    json.dumps(payload))
    log_api_call(
            method="PATCH",
            url=response.url,
            headers=response.headers,
            payload=payload,
            token=TOKEN,
            response=response
     )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_id")
    assert_response_status_code_custom_field(response.status_code,400)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC034_Actualizar_campo_con_ID_inexistente(get_url):
    """Descripcion el usuario no podra actualizar  un campo personalizado si pone un id que no existe"""

    payload = get_payload_by_id("title")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_valida")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                    StaticDataCustomField.patch_custom_field_no_existe.value,
                                    StaticDataHeaders.default_header.value,
                                    json.dumps(payload))
    log_api_call(
            method="PATCH",
            url=response.url,
            headers=response.headers,
            payload=payload,
            token=TOKEN,
            response=response
     )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_status_message_error")
    assert_response_status_code_custom_field(response.status_code,404)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC035_Peticion_sin_autenticacion(get_url):
    """Descripcion el usuario no podra actualizar  un campo personalizado si estar autenticado """

    payload = get_payload_by_id("title")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_valida")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                    StaticDataCustomField.patch_custom_field3.value,
                                    StaticDataHeaders.invalid_token_header.value,
                                    json.dumps(payload))
    log_api_call(
            method="PATCH",
            url=response.url,
            headers=response.headers,
            payload=payload,
            token=TOKEN_Invalido,
            response=response
     )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_message401")
    assert_response_status_code_custom_field(response.status_code,401)
def test_AE_TC036_Value_incompleto_en_payload(get_url):
    """Descripcion el usuario no podra actualizar  un campo personalizado si quiero añadir un valor y este solo tenga id y no titulo """

    payload = get_payload_by_id("AE_TC036")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_value_id")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                    StaticDataCustomField.patch_custom_field4.value,
                                    StaticDataHeaders.default_header.value,
                                    json.dumps(payload))
    log_api_call(
            method="PATCH",
            url=response.url,
            headers=response.headers,
            payload=payload,
            token=TOKEN,
            response=response
     )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_error_fields_status")
    assert_response_status_code_custom_field(response.status_code,400)
def test_AE_TC037_Actualizar_campo_personalizado_con_replace_values_con_valores_negativos(get_url):
    """Descripcion el usuario  podra actualizar  un campo personalizado si sus datos de values lleva titulo y id numeros negativos"""

    payload = get_payload_by_id("AE_TC037")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_value_id")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                    StaticDataCustomField.patch_custom_field2.value,
                                    StaticDataHeaders.default_header.value,
                                    json.dumps(payload))
    log_api_call(
            method="PATCH",
            url=response.url,
            headers=response.headers,
            payload=payload,
            token=TOKEN,
            response=response
     )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_valida")
    assert_response_status_code_custom_field(response.status_code,200)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.xfail(reason ="error permite dejar crear con codigos de proyecto que no existen  ", run=False)
def test_AE_TC038_Actualizar_campo_personalizado_con_projects_codes_inexistentes(get_url):
    """Descripcion el usuario no podra actualizar  un campo personalizado si pone un codigo de projecto que no existe"""

    payload = get_payload_by_id("AE_TC038")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_project_code")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                    StaticDataCustomField.patch_custom_field3.value,
                                    StaticDataHeaders.default_header.value,
                                    json.dumps(payload))
    log_api_call(
            method="PATCH",
            url=response.url,
            headers=response.headers,
            payload=payload,
            token=TOKEN,
            response=response
     )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_valida")
    assert_response_status_code_custom_field(response.status_code,404)

@pytest.mark.positive
@pytest.mark.regression
def test_AE_TC039_Value_numerico_y_titulo_en_formato_decimal(get_url):
    """Descripcion e actualizar  un campo personalizado con value id numero y titulo numero decimal"""

    payload = get_payload_by_id("AE_TC039")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_id_title")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                    StaticDataCustomField.patch_custom_field2.value,
                                    StaticDataHeaders.default_header.value,
                                    json.dumps(payload))
    log_api_call(
            method="PATCH",
            url=response.url,
            headers=response.headers,
            payload=payload,
            token=TOKEN,
            response=response
     )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_valida")
    assert_response_status_code_custom_field(response.status_code,200)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.xfail(reason ="error no deberia dejar poder actualizar datos  si en titulo ponemos un script ", run=False)
def test_AE_TC040_Inyeccion_XSS_en_title(get_url):
        """Descripcion el usuario no deberia poder poner un script  como titulo para un campo personalizado deberia dar error 400 """

        payload = get_payload_by_id("AE_TC040")
        assert_patch_custom_field_request_schema(payload, "schema_entrada_valida")
        response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                    StaticDataCustomField.patch_custom_field4.value,
                                    StaticDataHeaders.default_header.value,
                                    json.dumps(payload))
        log_api_call(
            method="PATCH",
            url=response.url,
            headers=response.headers,
            payload=payload,
            token=TOKEN,
            response=response
        )
        response_data = response.json()
        assert_patch_custom_field_response_schema(response_data, "schema_salida_valida")
        assert_response_status_code_custom_field(response.status_code, 400)

@pytest.mark.positive
@pytest.mark.regression
def test_AE_TC041_Inyeccion_SQL_en_title(get_url):
         """Descripcion el usuario  podra poner un comando de sql  en  campo personalizado como  titulo """

         payload = get_payload_by_id("AE_TC041")
         assert_patch_custom_field_request_schema(payload, "schema_entrada_valida")
         response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                        StaticDataCustomField.patch_custom_field1.value,
                                        StaticDataHeaders.default_header.value,
                                        json.dumps(payload))
         log_api_call(
                method="PATCH",
                url=response.url,
                headers=response.headers,
                payload=payload,
                token=TOKEN,
                response=response
          )
         response_data = response.json()
         assert_patch_custom_field_response_schema(response_data, "schema_salida_valida")
         assert_response_status_code_custom_field(response.status_code, 200)

@pytest.mark.negative
@pytest.mark.regression
@pytest.mark.xfail(reason ="error no acepta letras en value y no deja probarlo sale error en schema", run=False)
def test_AE_TC042_Value_con_letras_y_titulo_valido (get_url):
    """Descripcion el usuario  no podra actualizar  un campo personalizado si sus datos de values lleva titulo correcto y su  id es una letra"""

    payload = get_payload_by_id("AE_TC042")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_id_title",expect_error=True)
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.patch_custom_field2.value,
                                StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="PATCH",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_error_fields_status")
    assert_response_status_code_custom_field(response.status_code, 400)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC043_Value_numerico_y_titulo_que_excede_255_caracteres(get_url):
    """Descripcion el usuario no  podra actualizar  un campo personalizado si sus datos de values lleva un titulo que excede a la cantidad de 255 caracteres y id numeros """

    payload = get_payload_by_id("AE_TC043")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_value_id")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.patch_custom_field1.value,
                                StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="PATCH",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_error_fields_status")
    assert_response_status_code_custom_field(response.status_code, 400)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC044_Value_numerico_con_mas_de_19_digitos_y_titulo_valido(get_url):
    """Descripcion el usuario no podra actualizar  un campo personalizado si sus datos de values lleva titulo y id que exceda a 19 caracteres """

    payload = get_payload_by_id("AE_TC044")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_id_title")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.patch_custom_field1.value,
                                StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="PATCH",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_error_fields_status")
    assert_response_status_code_custom_field(response.status_code, 400)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC045_ID_en_formato_decimal_negativo(get_url):
    """Descripcion el usuario  podra actualizar  un campo personalizado si sus datos de values lleva titulo y id numeros negativos"""

    payload = get_payload_by_id("title_value")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_id_title")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.patch_custom_field_decimal_negativo.value,
                                StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="PATCH",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_id")
    assert_response_status_code_custom_field(response.status_code, 400)


@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC046_ID_en_formato_decimal_positivo (get_url):
    """Descripcion el usuario no  podra actualizar  un campo personalizado si la id es decimal positiva"""

    payload = get_payload_by_id("title_value")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_id_title")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.patch_custom_field_decimal_positivo.value,
                                StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="PATCH",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_id")
    assert_response_status_code_custom_field(response.status_code, 400)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC047_ID_numerico_negativo(get_url):
    """Descripcion el usuario no podra actualizar  un campo personalizado si la id es decimal negativo"""

    payload = get_payload_by_id("title_value")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_id_title")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.patch_custom_field_negativo.value,
                                StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="PATCH",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_id")
    assert_response_status_code_custom_field(response.status_code, 400)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC048_Peticion_sin_ID(get_url):
    """Descripcion el usuario no podra actualizar  un campo personalizado si intenta realizar una peticion sin id"""

    payload = get_payload_by_id("title_value")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_id_title")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.patch_custom_field_sin_id.value,
                                StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="PATCH",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_id")
    assert_response_status_code_custom_field(response.status_code, 400)


@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC049_ID_con_caracteres_especiales (get_url):
    """Descripcion el usuario no podra actualizar  un campo personalizado si intenta llamar un id con caracteres especiales"""

    payload = get_payload_by_id("title_value")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_id_title")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.patch_custom_field_simbolo.value,
                                StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="PATCH",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_id")
    assert_response_status_code_custom_field(response.status_code, 400)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC050_ID_con_codigo_XSS (get_url):
    """Descripcion al intentar realizar la peticion con un id que tiene un script con codigo xss este nos muestra un mensaje"""

    payload = get_payload_by_id("title_value")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_id_title")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.patch_script_custom_field.value,
                                StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="PATCH",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_message404")
    assert_response_status_code_custom_field(response.status_code, 404)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC051_is_visible_con_valor_no_booleano(get_url):
    """Descripcion el usuario no debe poner datos que no sean booleano en el valor de is visible """

    payload = get_payload_by_id("AE_TC051")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_is_visible")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.patch_custom_field1.value,
                                StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="PATCH",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_error_fields_status")
    assert_response_status_code_custom_field(response.status_code, 400)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC052_is_filterable_con_valor_no_booleano(get_url):
    """Descripcion  el usuario no debe poner datos que no sean booleano en el valor de is filterable"""

    payload = get_payload_by_id("AE_TC052")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_is_filterable")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.patch_custom_field1.value,
                                StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="PATCH",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_error_fields_status")
    assert_response_status_code_custom_field(response.status_code, 400)

@pytest.mark.negative
@pytest.mark.regression
def test_AE_TC053_is_required_con_valor_no_booleano(get_url):
    """Descripcion el usuario no debe poner datos que no sean booleano en el valor de is required"""

    payload = get_payload_by_id("AE_TC053")
    assert_patch_custom_field_request_schema(payload, "schema_entrada_is_required")
    response = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.custom_field.value,
                                StaticDataCustomField.patch_custom_field1.value,
                                StaticDataHeaders.default_header.value,
                                json.dumps(payload))
    log_api_call(
        method="PATCH",
        url=response.url,
        headers=response.headers,
        payload=payload,
        token=TOKEN,
        response=response
    )
    response_data = response.json()
    assert_patch_custom_field_response_schema(response_data, "schema_salida_error_fields_status")
    assert_response_status_code_custom_field(response.status_code, 400)
