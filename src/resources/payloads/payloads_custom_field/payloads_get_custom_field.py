import uuid

def generate_random_title(prefix: str = "custom_field") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:6]}"  # Ejemplo: custom_field_a1b2c3

payloads = {
    "AE_TC001": {
        "title": generate_random_title(),
        "entity": 0,
        "type": 0,
        "placeholder": "12",
        "default_value": "12"
    },
    "AE_TC002": {
        "entity": 10,
        "type": 10
    },
    "AE_TC003": {
        "title": generate_random_title(),
        "entity": 0,
        "type": 2
    },
    "AE_TC004": {
        "title": generate_random_title(),
        "entity": 1,
        "type": 10
    },
    "AE_TC005": {
        "title": generate_random_title(),
        "entity": 0,
        "type": 1
    },
    "AE_TC006": {
        "title": generate_random_title(),
        "entity": 0,
        "type": 1
    },
    "AE_TC007": {
        "title": generate_random_title(),
        "entity": 1,
        "type": 1
    },
    "AE_TC008": {
        "title": generate_random_title(),
        "entity": 2,
        "type": 1
    },
    "AE_TC009": {
        "title": generate_random_title(),
        "entity": 0,
        "type": 3,
        "value": [
            {"id": 1, "title": "prueba 1"},
            {"id": 2, "title": "prueba 2"}
        ]
    },
    "AE_TC010": {
        "title": generate_random_title(),
        "entity": 0,
        "type": 3
    },
    "AE_TC011": {
        "title": generate_random_title(),
        "entity": 0,
        "type": 5,
        "value": [
            {"id": 1, "title": "prueba 1"},
            {"id": 2, "title": "prueba 2"}
        ]
    },
    "AE_TC012": {
        "title": generate_random_title(),
        "entity": 0,
        "type": 5
    },
    "AE_TC013": {
        "title": generate_random_title(),
        "entity": 0,
        "type": 6,
        "value": [
            {"id": 1, "title": "prueba 1"},
            {"id": 2, "title": "prueba 2"}
        ]
    },
    "AE_TC014": {
        "title": generate_random_title(),
        "entity": 0,
        "type": 6
    },
    "AE_TC015": {
        "title": generate_random_title(),
        "entity": 0,
        "type": -1
    },
    "AE_TC016": {
        "title": generate_random_title(),
        "entity": 0,
        "type": 0
    },
    "AE_TC017": {
        "title": generate_random_title(),
        "entity": 0,
        "type": 9
    },
    "AE_TC018": {
        "title": generate_random_title(),
        "entity": 0,
        "type": 10
    },
    "AE_TC019": {
        "title": generate_random_title(),
        "entity": 0,
        "type": -2.5
    },
    "AE_TC020": {
        "title": generate_random_title(),
        "entity": 0,
        "type": 3.5
    },
}

def get_payload_by_id(test_case_id: str) -> dict:
    return payloads.get(test_case_id, {})
