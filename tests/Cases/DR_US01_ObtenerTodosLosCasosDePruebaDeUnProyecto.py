import requests
import src.common.config
URL = src.common.config.URL_CASE


def DR_TC01_Obtener_todo_los_test_case_de_un_proyecto ():
    headers = {
        'Token': 'b0753235e147cc7a6757233aaada6f3d9336bdb16b4383fdfd21c2dc65dc674f',
        'accept': 'application/json'
    }
    response = requests.get(URL, headers=headers)
    return response.status_code

if __name__ == "__main__":
    if 200 == DR_TC01_Obtener_todo_los_test_case_de_un_proyecto():
       print("paso la prueba")