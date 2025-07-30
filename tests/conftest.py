import pytest

from config import BASE_URI, TOKEN


@pytest.fixture(scope='session')
def get_url():
    return BASE_URI

@pytest.fixture(scope='session')
def get_token():
    return TOKEN