import pytest



from config import *
from src.headers.headers import *




@pytest.fixture(scope='session')
def get_url():
    return BASE_URI

@pytest.fixture(scope='session')
def get_invalid_url():
    return BASE_INVALID_URI

@pytest.fixture(scope='session')
def get_token():
    return get_header_with_token()

@pytest.fixture(scope='session')
def get_headers():
    return get_header_without_token()


@pytest.fixture(scope='session')
def get_headers_no_accept():
    return get_header_without_accept()

@pytest.fixture(scope='session')
def get_headers_no_content():
    return get_header_without_content()


