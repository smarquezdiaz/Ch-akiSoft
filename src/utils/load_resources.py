import pytest
import requests
import json

@pytest.fixture()
def load_payload_resource(json):
    json_string = json
    datos = json.loads(json_string)