import json
import os
import jsonschema
import pytest
import requests
def assert_response_status_code(status_code, expected_code):
    assert status_code == expected_code, f"Status esperado {expected_code}, Status obtenido {status_code}"

def assert_response_status_code_global(expected_code, status_code):
        assert status_code == expected_code, f"Status esperado {expected_code}, Status obtenido {status_code}"

def assert_equals(result, expected_result):
    assert result == expected_result, f"Resultado esperado {result}, resultado obtenido {expected_result}"

def assert_get_cases_assertion(method, url, headers, payload=None):
    response = requests.request(method, url, headers=headers, data=payload)
    return response