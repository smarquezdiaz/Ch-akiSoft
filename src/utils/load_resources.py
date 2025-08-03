import json
import os

def load_schema_resource(json_name):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    file_path = os.path.join(base_dir, 'src', 'resources', 'schemas', json_name)
    with open(file_path) as schema_file:
        return json.load(schema_file)

def load_schema_resource1(json_name,schema_key=None):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    file_path = os.path.join(base_dir, 'src', 'resources', 'schemas', 'schema_custom_fields', f"{json_name}.json")
    with open(file_path, 'r', encoding='utf-8') as schema_file:
        all_schemas = json.load(schema_file)

    if schema_key:
        if schema_key not in all_schemas:
            raise ValueError(f"Schema '{schema_key}' no encontrado en el archivo {json_name}.json")
        return all_schemas[schema_key]

    return all_schemas


