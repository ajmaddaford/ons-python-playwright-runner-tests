import pytest
from playwright.sync_api import Page
from utils import generate_token


@pytest.fixture(scope='session')
def base_url():
    return 'http://localhost:5000/'

@pytest.fixture
def open_questionnaire(page: Page):

    def _open_questionnaire(schema: str):
        token = generate_token(schema)
        url = f"/questionnaire/?token={token}"
        page.goto(url, wait_until="networkidle")
    
    return _open_questionnaire
