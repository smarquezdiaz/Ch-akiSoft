import pytest
import requests

@pytest.mark.smoke
@pytest.mark.regression
def test_GC001_Obtener_todos_los_proyectos_existentes():
    #url = f"{get_url}/project"
    token = "a3b83af57ac9486e9e1402b0aa8aca01c905c976edaa3ff1888221ffb0e2326b"
    url = "https://api.qase.io/v1/project?limit=100&offset=0"

    headers = {
        'Token': token,
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200