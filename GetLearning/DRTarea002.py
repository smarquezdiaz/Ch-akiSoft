import pytest
import requests

@pytest.mark.smoke
def DR_Tarea_002_Obtener_el_error_404():
    """El usuario debe obtener un error 404 cuando solicita información de un objeto que no existe"""
    object_id = "999999999"
    """
    pasos
    1 entrar a postman
    2 seleccionar get
    3 llenar el object id con un id que no existe
    4 clic en send
    5 verificar que el estado esa 404
    """
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
    response = requests.get(url)
    assert response.status_code == 404
    """prioridad media, resultado esperado obtener una respuesta 404"""

@pytest.mark.smoke
def DR_Tarea_003_Obtener_el_error_400():
    """El usuario debe obtener un error 400 cuando hace una petición mal formada ID no numérico"""
    object_id = "abc"
    """
        pasos
        1 entrar a postman
        2 seleccionar get
        3 llenar el object id con un id de solo letras
        4 clic en send
        5 verificar que el estado esa 400
        """
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
    response = requests.get(url)
    assert response.status_code == 400
    """prioridad media, resultado esperado obtener una respuesta 400"""