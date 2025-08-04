import json
import os
def load_schema(schema_name):
    base_path = os.path.dirname(os.path.dirname(__file__))
    schema_path = os.path.join(base_path, "resources", "schemas", f"{schema_name}.json")
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)