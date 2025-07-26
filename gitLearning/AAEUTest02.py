import pytest
import requests
import json
@pytest.mark.smoke
#id AAEU-02
#prioridad media
def test_02_error404 ():
    """Descripción:nos debe mostrar el error al actualizar un id de un archivo borrado """
# ambiente
url = "https://api.restful-api.dev/objects/ff8081819782e69e019843f257bc2757"

#paso 1 añadir  un equipo nuevo
# paso 2 añadir los payload para un equipo nuevo
payload = json.dumps({
  "name": "Apple  20",
  "data": {
    "year": 2019,
    "price": 1849.99,
    "CPU model": "Intel Core i9",
    "Hard disk size": "1 TB"
  }
#paso 3 añadir headers que nos solicita
})
headers = {
  'Content-Type': 'application/json'
}
#resultado esperado utilizar el metodo put para buscar el equipo usando headers y payload
response = requests.request("PUT", url, headers=headers, data=payload)
# verificar que se muestre el error 404 por buscar un archivo que no existe
assert response.status_code == 404
print(response.text)
