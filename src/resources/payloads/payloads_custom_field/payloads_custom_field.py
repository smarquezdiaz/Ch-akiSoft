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
    "AE_TCe2e": {
        "title": generate_random_title(),
        "entity": 0,
        "type": 0
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
    "AE_TC030": {
        "title": generate_random_title()
    },
    "title": {
        "title": generate_random_title()
    },
    "AE_TC031": {
    "title": " "
    },
    "AE_TC032": {
        "title": "ZaJWGwhkyVRpRNNcFHyLviReMYAeHERSQBtBgqTMNNdcuSTrexMHWDBGAutkyFKVPiPrxGKvEkqvxiuMLxvKGtiKvbjqevPqucmTfFBahaAnUrhnZdzpiXKVxvkqqZjJcrmJDdUdcrrugRzVabFjyhXkVGQQkMmyLRzhegRYLUYcvqdKrrkVrpvuKZHQMySpKNHTzLYeDdUGjdnVVCgTpHGLUDbeQptSZGgNnGYGTfzHCDapqazyarmkhWWkCaT1d"
    },

    "AE_TC036": {
        "title": generate_random_title(),
        "value": [
            {
                "id": -1

            }
        ]
    },
    "AE_TC037": {
        "title": generate_random_title(),
        "value": [
            {
            "id": -1,
            "title": "-1"
            }
        ]
    },
    "AE_TC038": {
        "title": generate_random_title(),
        "projects_codes": [
        "ejemplo2"
    ]
    },
    "AE_TC039": {
        "title": generate_random_title(),
        "value": [
            {
            "id": -1,
            "title": "-1"
            }
        ]
    },
    "AE_TC040": {
        "title": "<script>alert('XSS')</script>"
    },

    "AE_TC041": {
        "title": "1 OR 1=1; DROP TABLE users"
    },
    "AE_TC042": {
        "title": generate_random_title(),
    "value": [
    {
      "id": "a",
      "title": "pruebas 7"
    }
    ]
    },
    "AE_TC043": {
    "title": generate_random_title(),
    "value": [
    {
      "title": "ZaJWGwhkyVRpRNNcFHyLviReMYAeHERSQBtBgqTMNNdcuSTrexMHWDBGAutkyFKVPiPrxGKvEkqvxiuMLxvKGtiKvbjqevPqucmTfFBahaAnUrhnZdzpiXKVxvkqqZjJcrmJDdUdcrrugRzVabFjyhXkVGQQkMmyLRzhegRYLUYcvqdKrrkVrpvuKZHQMySpKNHTzLYeDdUGjdnVVCgTpHGLUDbeQptSZGgNnGYGTfzHCDapqazyarmkhWWkdfff",
      "id": 1
    }
    ]
    },
    "title_value": {
        "title": generate_random_title(),
        "value": [
    {
      "title": "prueba12",
      "id": 111111111
    }

    ]
    },
    "AE_TC044": {
        "title": generate_random_title(),
        "value": [
    {
      "title": "prueba12",
      "id": 111111111111111111111
    }]
    },

    "AE_TC051": {
        "title": generate_random_title(),
        "is_visible": "abc"

    },
    "AE_TC052": {
        "title": generate_random_title(),
        "is_filterable": "abc"

    },
    "AE_TC053": {
        "title": generate_random_title(),
        "is_required": "abc"

    },

}

def get_payload_by_id(test_case_id: str) -> dict:
    return payloads.get(test_case_id, {})
