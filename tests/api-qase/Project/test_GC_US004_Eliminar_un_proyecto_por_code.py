import pytest

from config import TOKEN
from src.common.logger import log_api_call
from src.common.static_data_modules import StaticDataModules
from src.common.static_data_project import StaticDataProject, StaticDataProjectPorCode, StaticDataProjectDeletePorCode
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.utils.api_calls import request_function
from src.assertions.global_assertions import assert_response_schema, assert_response_status_code_global


#Alta
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_GCTC001_Verificar_que_se_elimine_un_proyecto_exitosamente_con_un_código_válido(get_url, setup_add_project):
        """
        Descripción: Verificar que el servicio API de Qase permite eliminar un proyecto existente cuando se proporciona un código válido.
        """
        id_to_delete = setup_add_project["result"]["code"]
        response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                    f"/{id_to_delete}", StaticDataHeaders.default_header.value)
        log_api_call(method="GET",
                     url=response.url,
                     headers=response.headers,
                     payload=None,
                     token=TOKEN,
                     response=response
                     )
        assert_response_schema(response.json(), "delete_project_response.json", "schemas_project")
        assert_response_status_code_global(200, response.status_code)


#Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC002_Verificar_que_retorne_error_404_al_enviar_un_código_de_proyecto_con_menos_de_2_caracteres(get_url):
    """
    Descripción: Verificar que el API no permita eliminar un proyecto cuando el código tiene menos de 2 caracteres.
    """
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                StaticDataProjectDeletePorCode.invalid_code_param_delete_1.value, StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "delete_erro404_response.json", "schemas_project")
    assert_response_status_code_global(404, response.status_code)


#Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC003_Verificar_que_retorne_error_404_al_enviar_un_código_de_proyecto_con_más_de_10_caracteres(get_url):
    """
    Descripción: Verificar que el API no permita eliminar un proyecto cuando el código tiene menos de 2 caracteres.
    """
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                StaticDataProjectDeletePorCode.invalid_code_param_delete_10.value, StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "delete_erro404_response.json", "schemas_project")
    assert_response_status_code_global(404, response.status_code)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC004_Verificar_que_retorne_error_405_al_enviar_un_código_vacío(get_url):
    """
    Descripción: Confirmar que el API no permite eliminar un proyecto si no se envía el código.
    """
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                StaticDataProjectDeletePorCode.invalid_code_param_delete.value, StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_error405_project_response_by_code.json", "schemas_project")
    assert_response_status_code_global(405, response.status_code)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC005_Verificar_que_retorne_error_404_al_intentar_eliminar_un_proyecto_inexistente(get_url):
    """
    Descripción: Validar que el API devuelva "Not Found" al intentar eliminar un proyecto que no existe.
    """
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                StaticDataProjectDeletePorCode.invalid_code_param_delete_no.value, StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_error404_project_response.json", "schemas_project")
    assert_response_status_code_global(404, response.status_code)

#Alta
@pytest.mark.regression
@pytest.mark.negative
@pytest.mark.high
def test_GCTC006_Verificar_que_retorne_error_401_al_intentar_eliminar_un_proyecto_sin_autenticación(get_url, setup_add_project):
    """
    Descripción: Validar que no se pueda eliminar un proyecto si no se envía token de autorización.
    """
    id_to_delete = setup_add_project["result"]["code"]
    response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,
                                f"/{id_to_delete}",
                                StaticDataHeaders.no_token_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_error401_project_response.json", "schemas_project")
    assert_response_status_code_global(401, response.status_code)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC007_Verificar_que_retorne_error_401_al_intentar_eliminar_un_proyecto_con_una_URL_mal_escrita(get_invalid_url, setup_add_project):
    """
    Descripción: Confirmar que la API devuelva error al usar una ruta mal escrita.
    """
    id_to_delete = setup_add_project["result"]["code"]
    response = request_function(StaticDataVerbs.get.value, get_invalid_url, StaticDataModules.project.value,
                                f"/{id_to_delete}",
                                StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_error404_project_response.json", "schemas_project")
    assert_response_status_code_global(404, response.status_code)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC008_Verificar_que_retorne_error_al_enviar_un_código_de_proyecto_con_caracteres_especiales(get_url):
    """
    Descripción: Confirmar que la API rechace códigos con caracteres no permitidos.
    """
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                StaticDataProjectDeletePorCode.invalid_code_param_delete_spacial.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_error404_project_response.json", "schemas_project")
    assert_response_status_code_global(404, response.status_code)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC009_Verificar_que_retorne_error_al_enviar_un_código_de_proyecto_numérico(get_url):
    """
    Descripción: Validar que la API no acepte códigos puramente numéricos si la validación lo prohíbe.
    """
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                StaticDataProjectDeletePorCode.invalid_code_param_delete_number.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_error404_project_response.json", "schemas_project")
    assert_response_status_code_global(404, response.status_code)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC010_Verificar_que_retorne_error_al_enviar_un_código_de_proyecto_con_espacios(get_url):
    """
    Descripción: Confirmar que no se pueda eliminar un proyecto si el código contiene espacios.
    """
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                StaticDataProjectDeletePorCode.invalid_code_param_delete_space.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_error404_project_response.json", "schemas_project")
    assert_response_status_code_global(404, response.status_code)

#Alta
@pytest.mark.smoke
@pytest.mark.positive
def test_GCTC011_Verificar_que_se_elimine_un_proyecto_con_código_en_mayúsculas(get_url, setup_add_project):
    """
    Descripción: Confirmar que el API permita eliminar un proyecto cuyo código esté en mayúsculas.
    """
    id_to_delete = setup_add_project["result"]["code"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                f"/{id_to_delete}", StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "delete_project_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)

#Media
@pytest.mark.smoke
@pytest.mark.positive
def test_GCTC012_Verificar_que_se_elimine_un_proyecto_con_código_en_minúsculas(get_url, setup_add_project):
    """
    Descripción: Confirmar que se pueda eliminar un proyecto usando código en minúsculas.
    """
    id_to_delete = setup_add_project["result"]["code"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                f"/{id_to_delete}", StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "delete_project_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)

#Media
@pytest.mark.smoke
@pytest.mark.positive
def test_GCTC013_Verificar_que_se_elimine_un_proyecto_cuyo_código_tenga_exactamente_2_caracteres(get_url, setup_add_project_2_character):
    """
    Descripción: Validar que la API acepte el mínimo de caracteres permitidos para eliminar un proyecto.
    """
    id_to_delete = setup_add_project_2_character["result"]["code"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                f"/{id_to_delete}", StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "delete_project_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)

#Media
@pytest.mark.smoke
@pytest.mark.positive
def test_GCTC014_Verificar_que_se_elimine_un_proyecto_cuyo_código_tenga_exactamente_10_caracteres(get_url, setup_add_project_10_character):
    """
    Descripción: Validar que la API acepte el máximo permitido de caracteres.
    """
    id_to_delete = setup_add_project_10_character["result"]["code"]
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                f"/{id_to_delete}", StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "delete_project_response.json", "schemas_project")
    assert_response_status_code_global(200, response.status_code)

#Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC015_Verificar_que_retorne_error_al_intentar_eliminar_un_proyecto_y_eliminado_previamente(get_url, setup_add_project_10_character):
    """
    Descripción: Validar que no se pueda volver a eliminar un proyecto inexistente tras haber sido borrado.
    """
    id_to_delete = setup_add_project_10_character["result"]["code"]

    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                f"/{id_to_delete}", StaticDataHeaders.default_header.value)
    response2 = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                f"/{id_to_delete}", StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_error404_project_response.json", "schemas_project")
    assert_response_status_code_global(404, response2.status_code)


#Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC016_Verificar_que_retorne_error_al_enviar_un_código_de_proyecto_nulo(get_url):
    """
    Descripción: Confirmar que la API no acepte código nulo.
    """
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                f"/{StaticDataProjectDeletePorCode.invalid_code_param_delete_none.value}", StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "delete_erro404_response.json", "schemas_project")
    assert_response_status_code_global(404, response.status_code)


#Media
@pytest.mark.regression
@pytest.mark.positive
def test_GCTC017_Verificar_error_al_eliminar_un_code_con_desimales(get_url):
    """
    Verificar que el sistema no permita eliminar un code con desimales
    """
    response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                StaticDataProjectDeletePorCode.invalid_code_param_delete_decimal.value,
                                StaticDataHeaders.default_header.value)
    log_api_call(method="GET",
                 url=response.url,
                 headers=response.headers,
                 payload=None,
                 token=TOKEN,
                 response=response
                 )
    assert_response_schema(response.json(), "get_error404_project_response.json", "schemas_project")
    assert_response_status_code_global(404, response.status_code)