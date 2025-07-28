import requests
import json
import pytest

from src.config.config import URL_CASE


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_001_Crear_un_test_case():

    url = URL_CASE

    list_url = url

    payload = json.dumps({
      "title": "Verificar que funciona el qase 3 xd",
      "suite_id": 1
    })
    headers = {
      'Token': '0cfe63bf6fab9cc50b29d323d96e1376251d2a9bf0cdb07accc5bedc3088a2c5',
      'accept': 'application/json',
      'content-type': 'application/json'
    }

    response = requests.request("POST", list_url, headers=headers, data=payload)

    assert response.status_code == 200
