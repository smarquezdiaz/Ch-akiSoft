import json

import pytest
import requests

from src.common.config import URL_CASE, TOKEN_SOL


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_001_Crear_un_test_case():

    url = URL_CASE

    token = TOKEN_SOL

    payload = json.dumps({
      "title": "Verificar la verificacion 2",
      "suite_id": 1
    })
    headers = {
      'Token': token,
      'accept': 'application/json',
      'content-type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.status_code == 200
