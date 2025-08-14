import random
import string
def assert_request_plan_payload(
        title: str | int | None = None,
        description: str | int | None = None,
        cases: list[int] | None = None
) -> dict:
    #Genera un payload para crear un plan .
    actual_title = get_random_title() if title is None else title
    payload = {
        "title": actual_title,
        "description": get_random_property() if description is None else description,
        "cases": [11] if cases is None else cases
    }
    return payload

def get_random_title():
    #Genera un título aleatorio de 5 caracteres alfanuméricos.
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

def get_random_property():
    #Genera una cadena aleatoria de 100 caracteres alfanuméricos.
    return ''.join(random.choices(string.ascii_letters + string.digits, k=100))