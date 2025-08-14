from src.common.static_data_modules import StaticDataModules
from src.common.static_data_suites import StaticDataSuites


def assert_200_schema_items(id, status, id_to_delete):
    assert id == id_to_delete
    assert status == True

def assert_not_found_route_schema_items(response, id_to_delete):
    assert response.json()["message"] == f"The route api/v1/{StaticDataModules.suite.value}{StaticDataSuites.invalid_url_suffix_for_404.value}/{id_to_delete} could not be found."

def assert_unauthenticated_schema_items(response):
    assert response.json()["error"] == "Unauthenticated."

def project_not_found_schema_items(response):
    assert response.json()["errorMessage"] == "Project not found"

def assert_method_not_supported_schema_items(response, id_to_delete):
    assert response.json()["message"] == f"The DELETE method is not supported for route api/v1/{StaticDataModules.suite.value}/{id_to_delete}. Supported methods: GET, HEAD, POST."

def assert_method_not_supported_and_id_empty_schema_items(response):
    assert response.json()["message"] == f"The DELETE method is not supported for route api/v1/{StaticDataModules.suite.value}{StaticDataSuites.default_url_suffix.value}. Supported methods: GET, HEAD, POST."

def suite_not_found_schema_items(response):
    assert response.json()["errorMessage"] == "Suite not found"

def suite_destination_id_invalid_schema_items(response):
    assert response.json()["errorMessage"] == "Destination id is not valid"