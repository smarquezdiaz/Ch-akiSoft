import pytest

from config import BASE_URI, TOKEN
from src.headers.headers import get_header_with_token, get_header_without_token


@pytest.fixture(scope='session')
def get_url():
    return BASE_URI

@pytest.fixture(scope='session')
def get_token():
    return get_header_with_token()

@pytest.fixture(scope='session')
def get_headers():
    return get_header_without_token()