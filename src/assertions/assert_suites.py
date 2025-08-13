import re


def validate_path_params(id_to_delete, type):
    assert type(id_to_delete) == type

def validate_url_params(url):
    assert re.search(r"id=\d+", url)
    assert re.search(r"name=[A-Za-z]+", url)