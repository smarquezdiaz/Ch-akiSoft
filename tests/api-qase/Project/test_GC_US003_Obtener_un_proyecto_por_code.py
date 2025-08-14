import pytest

from config import TOKEN
from src.common.logger import log_api_call
from src.common.static_data_modules import StaticDataModules
from src.common.static_data_project import StaticDataProject, StaticDataProjectPorCode
from src.common.static_headers import StaticDataHeaders
from src.common.static_verbs import StaticDataVerbs
from src.utils.api_calls import request_function
from src.utils.load_resources import assert_response_schema, assert_response_status_code_global


#Alta
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_GCTC001_Obtener_un_proyecto_existente_con_codigo_valido(get_url):
        """
        Descripción: Verificar que el servicio API de Qase responde correctamente con la información del proyecto cuando se consulta con un code válido.
        """
        response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,
                                    StaticDataProjectPorCode.valid_code_param.value, StaticDataHeaders.default_header.value)
        log_api_call(method="GET",
                     url=response.url,
                     headers=response.headers,
                     payload=None,
                     token=TOKEN,
                     response=response
                     )
        assert_response_schema(response.json(), "get_project_response_by_code.json", "schemas_project")
        assert_response_status_code_global(200, response.status_code)

# Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC002_URL_mal_formada(get_url):
        """
        Descripción: Validar que el servicio retorna error cuando la URL del recurso está mal escrita.
        """
        response = request_function(StaticDataVerbs.get.value ,get_url, StaticDataModules.project.value ,StaticDataProjectPorCode.invalid_url_code.value, StaticDataHeaders.default_header.value)
        log_api_call(method="GET",
                     url= response.url,
                     headers=response.headers,
                     payload=None,
                     token=TOKEN,
                     response=response
                     )
        assert_response_schema(response.json(), "get_error404_project_response.json", "schemas_project")
        assert_response_status_code_global(404, response.status_code)

# Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC003_Token_incorrecto(get_url):
        """
        Descripción: Verificar que la API deniegue la solicitud con credenciales inválidas.
        """
        response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,
                                    StaticDataProjectPorCode.valid_code_param.value,
                                    StaticDataHeaders.invalid_token_header.value)
        log_api_call(method="GET",
                     url=response.url,
                     headers=response.headers,
                     payload=None,
                     token=TOKEN,
                     response=response
                     )
        assert_response_schema(response.json(), "get_error401_project_response.json", "schemas_project")
        assert_response_status_code_global(401, response.status_code)

# Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC004_Proyecto_inexistente(get_url):
        """
        Descripción: Verificar que la API retorne error cuando el proyecto no existe.
        """
        response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,
                                    StaticDataProjectPorCode.invalid_no_exist_code.value,
                                    StaticDataHeaders.default_header.value)
        log_api_call(method="GET",
                     url=response.url,
                     headers=response.headers,
                     payload=None,
                     token=TOKEN,
                     response=response
                     )
        assert_response_schema(response.json(), "get_error500_project_response_by_code.json", "schemas_project")
        assert_response_status_code_global(500, response.status_code)


#Alta
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_GCTC005_Obtener_un_proyecto_con_codigo_en_mayusculas(get_url):
        """
        Descripción: Confirmar que códigos en mayúsculas son aceptados.
        """
        response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,
                                    StaticDataProjectPorCode.valid_code_param.value, StaticDataHeaders.default_header.value)
        log_api_call(method="GET",
                     url=response.url,
                     headers=response.headers,
                     payload=None,
                     token=TOKEN,
                     response=response
                     )
        assert_response_schema(response.json(), "get_project_response_by_code.json", "schemas_project")
        assert_response_status_code_global(200, response.status_code)

# Media
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_GCTC006_Obtener_un_proyecto_con_codigo_en_minusculas(get_url):
        """
        Descripción: Confirmar que códigos en minúsculas son aceptados.
        """
        response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,
                                    StaticDataProjectPorCode.valid_code_param.value, StaticDataHeaders.default_header.value)
        log_api_call(method="GET",
                     url=response.url,
                     headers=response.headers,
                     payload=None,
                     token=TOKEN,
                     response=response
                     )
        assert_response_schema(response.json(), "get_project_response_by_code.json", "schemas_project")
        assert_response_status_code_global(200, response.status_code)

# Media
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_GCTC007_Obtener_un_proyecto_con_codigo_minimo_valido_2(get_url):
        """
        Descripción: Verificar que la API retorna el proyecto cuando el code tiene 2 caracteres.
        """
        response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,
                                    StaticDataProjectPorCode.valid_code_param.value, StaticDataHeaders.default_header.value)
        log_api_call(method="GET",
                     url=response.url,
                     headers=response.headers,
                     payload=None,
                     token=TOKEN,
                     response=response
                     )
        assert_response_schema(response.json(), "get_project_response_by_code.json", "schemas_project")
        assert_response_status_code_global(200, response.status_code)

# Media
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_GCTC008_Obtener_un_proyecto_con_codigo_maximo_valido_10(get_url):
        """
        Descripción: Verificar respuesta correcta con code de 10 caracteres.
        """
        response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,
                                    StaticDataProjectPorCode.valid_code_param.value, StaticDataHeaders.default_header.value)
        log_api_call(method="GET",
                     url=response.url,
                     headers=response.headers,
                     payload=None,
                     token=TOKEN,
                     response=response
                     )
        assert_response_schema(response.json(), "get_project_response_by_code.json", "schemas_project")
        assert_response_status_code_global(200, response.status_code)



# Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC009_Codigo_de_1_caracter(get_url):
        """
        Descripción: Validar que se retorne error por longitud mínima inválida.
        """
        response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,
                                    StaticDataProjectPorCode.invalid_code_param.value,
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

# Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC010_Verificar_que_no_permita_obtener_un_proyecto_con_código_de_más_de_10_aracteres(get_url):
        """
        Descripción: Validar que se retorne error por exceder longitud máxima.
        """
        response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,
                                    StaticDataProjectPorCode.invalid_code_param_mas_limit.value,
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

# Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC011_Verificar_que_no_permita_obtener_un_proyecto_con_código_vacío(get_url):
        """
        Descripción: Validar que la API rechace un código vacío.
        """
        response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,
                                    StaticDataProjectPorCode.invalid_code_param_null.value,
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

# Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC012_Verificar_que_no_permita_obtener_un_proyecto_con_caracteres_especiales_en_el_código(get_url):
        """
        Descripción: Confirmar que la API rechaza códigos con caracteres especiales.
        """
        response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,
                                    StaticDataProjectPorCode.invalid_code_param_special.value,
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

# Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC013_Verificar_que_no_permita_obtener_un_proyecto_con_espacios_en_el_código(get_url):
        """
        Descripción: Confirmar que la API rechaza códigos con espacios.
        """
        response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,
                                    StaticDataProjectPorCode.invalid_code_param_space.value,
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

# Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC014_Error_al_obtener_un_proyecto_con_código_numérico_válido(get_url):
        """
        Descripción: Validar que un code únicamente numérico no sea aceptado.
        """
        response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,
                                    StaticDataProjectPorCode.invalid_code_param_number.value,
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

# Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC015_Verificar_que_sin_header_token_se_devuelva_error(get_url):
        """
        Descripción: Asegurar que el endpoint exige autenticación.
        """
        response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,
                                    StaticDataProjectPorCode.valid_code_param.value,
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

# Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC016_Verificar_que_se_devuelva_error_405_si_se_usa_método_POST_en_lugar_de_GET(get_url):
        """
        Descripción: Verificar que el endpoint no permite POST.
        """
        response = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.project.value,
                                    StaticDataProjectPorCode.valid_code_param.value,
                                    StaticDataHeaders.default_header.value)
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
def test_GCTC017_Verificar_que_se_devuelva_error_405_si_se_usa_método_DELETE_en_lugar_de_GET(get_url):
        """
        Descripción: Verificar que el endpoint no permite DELETE.
        """
        response = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.project.value,
                                    StaticDataProjectPorCode.valid_code_param2.value,
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


# Media
@pytest.mark.regression
@pytest.mark.negative
def test_GCTC018_Obtener_un_proyecto_sin_autentificarse(get_url):
        """
        Descripción: Verificar que la API deniegue la solicitud cuando no se proporciona autenticación válida (sin sesión/autorización).
        """
        response = request_function(StaticDataVerbs.get.value, get_url, StaticDataModules.project.value,
                                    StaticDataProjectPorCode.valid_code_param.value,
                                    StaticDataHeaders.no_content_header.value)
        log_api_call(method="GET",
                     url=response.url,
                     headers=response.headers,
                     payload=None,
                     token=TOKEN,
                     response=response
                     )
        assert_response_schema(response.json(), "get_error404_project_response_exclusive.json", "schemas_project")
        assert_response_status_code_global(404, response.status_code)



