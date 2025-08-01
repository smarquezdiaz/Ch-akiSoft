import json
import os

def load_schema_resource(json_name):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    file_path = os.path.join(base_dir, 'src', 'resources', 'schemas', json_name)
    with open(file_path) as schema_file:
        return json.load(schema_file)
