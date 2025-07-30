import pytest
import requests

@pytest.mark.smoke
@pytest.mark.regression
def test_SM001_Obtener_todos_los_casos_de_prueba(get_url, get_token):
    url = f"{get_url}/suite/DEMO"
    token = get_token

    headers = {
        'Token': token,
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200