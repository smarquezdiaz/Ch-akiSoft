import pytest
import requests


@pytest.mark.smoke
def US001_01_Obtener_los_datos_del_objeto_con_el_ID_1():
    id = "1"
    """El usuario debe obtener la información del objeto 1 como el año en el que ingreso al museo, su código interno, si es de dominio público, su id, su nombre, su link de wikidata, su rol, el nombre del artista quien lo creo, la nacionalidad del artista, la fecha de nacimiento y muerte del artista"""
    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"
    list_url = url + id
    response = requests.get(list_url)
    assert response.status_code == 200
    """prioridad media, resultado esperado obtener una respuesta 200"""