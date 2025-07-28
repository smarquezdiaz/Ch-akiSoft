import pytest
import requests

@pytest.mark.smoke
def test_001_Obtener_la_lista_de_secciones_del_sistema():
    # Descripción: Verificar que el usuario pueda obtener la listas de secciones.

    #Ambiente
    url = "https://api.todoist.com"
    #Pasos
    #Abrir Postman
    #Copiar URL
    #Seleccionar método GET
    #Agregar headers de autorizacion
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 636d85f1f3f0fe9ba6a2dfcba0d580f58469c7c2',
        'Cookie': 'tduser=v4.public.eyJ1c2VyX2lkIjogNDQwOTAxMDUsICJleHAiOiAiMjAyNS0wOC0wNVQyMjo1NjowMCswMDowMCJ9ZIiSncQH2aaD-OywQY4t6ItBtOLO8c_Nc9cu0xYESaM5mFh8cvEaMGni9TEnIsKZhDj9h7I1zZ2zL-HNlvkuAQ; todoistd="/CUdA09psYiwY7pwgn9sRGC/RQQ=?"; csrf=f6c18d0a95f5432cb2979945a37c4a11'
    }
    list_url = url + "/api/v1/sections"


    response = requests.get(list_url, headers=headers)

    # Verificar que la respuesta sea correcta con status 200
    assert response.status_code == 200