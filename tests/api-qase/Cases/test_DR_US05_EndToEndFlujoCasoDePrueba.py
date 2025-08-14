
from tests.conftest import get_url
from src.common.logger import log_api_call
from src.common.static_verbs import StaticDataVerbs
from src.common.static_data_suites import StaticDataSuites
from src.common.static_data_modules import StaticDataModules
from src.common.static_headers import StaticDataHeaders
from src.utils.api_calls import request_function
from src.assertions.get_cases_assertions import *
from src.common.url import case_patch_join
from src.resources.payloads.payloads_case.payloads_post_case import *

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_DR_TC107_Verificar_el_flujo_completo_de_un_caso_de_prueba(get_url):
    #Post crear un caso de prueba solo con el nombre por que tenia prisa el usuario
    request_post = case_request_payload(title=name_random_cases())
    response_post = request_function(StaticDataVerbs.post.value, get_url, StaticDataModules.case.value,StaticDataSuites.default_url_suffix.value,header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request_post))
    log_api_call(method=StaticDataVerbs.post.value, url=response_post.url, headers=response_post.headers,payload=request_post, token=response_post.request.headers.get("Token"), response=response_post)
    #Guaradamos el ID
    save_ID = response_post.json()["result"]["id"]
    #Patch editar los campos severidad,prioridad,tipo,status y automation
    request_patch = case_request_payload(name_random_cases(), random_severity_case(), random_priority_case(),random_type_case(), random_status_case(), random_automation_case())
    response_patch = request_function(StaticDataVerbs.patch.value, get_url, StaticDataModules.case.value,case_patch_join(StaticDataSuites.default_url_suffix.value, save_ID),header_type=StaticDataHeaders.default_header.value, payload=json.dumps(request_patch))
    log_api_call(method=StaticDataVerbs.delete.value, url=response_patch.url, headers=response_patch.headers,payload=request_patch, token=response_patch.request.headers.get("Token"), response=response_patch)
    #Eliminar el caso de prueba
    response_delete = request_function(StaticDataVerbs.delete.value, get_url, StaticDataModules.case.value,case_patch_join(StaticDataSuites.default_url_suffix.value, save_ID),header_type=StaticDataHeaders.default_header.value)
    log_api_call(method=StaticDataVerbs.delete.value,url=response_delete.url,headers=response_delete.headers,payload=None,token=response_delete.request.headers.get("Token"),response=response_delete)
    assert_response_status_code_case(response_delete.status_code, 200)