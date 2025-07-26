import pytest
import requests

@pytest.mark.negative
def test_003_Verificar_error_405_al_usar_método_incorrecto():
    # Descripción: Verificar que el API del museo devuelve el código 405 cuando se utiliza el método POST en un endpoint que solo admite GET
    url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
    response = requests.post(url)

    assert response.status_code == 405

#priodad : Media