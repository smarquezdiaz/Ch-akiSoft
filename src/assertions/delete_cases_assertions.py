
import requests

def assert_delete_cases_assertion(get_url, get_token, code):
    url = f"{get_url}/case/{code}"
    token = get_token

    headers = {
        'Token': token,
        'accept': 'application/json'
    }

    response = requests.delete(url, headers=headers)
    return response