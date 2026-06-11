import pytest
import os
from playwright.sync_api import Page
from sdc.crypto.key_store import KeyStore
from token_generator import TokenGenerator


KEY_PURPOSE_AUTHENTICATION = "authentication"
EQ_USER_AUTHENTICATION_RRM_PRIVATE_KEY_KID = "709eb42cfee5570058ce0711f730bfbb7d4c8ade"
SR_USER_AUTHENTICATION_PUBLIC_KEY_KID = "e19091072f920cbf3ca9f436ceba309e7d814a62"

KEYS_FOLDER = "./jwt-test-keys"


def get_file_contents(filename, trim=False):
    with open(os.path.join(KEYS_FOLDER, filename), "r", encoding="utf-8") as f:
        data = f.read()
        if trim:
            data = data.rstrip("\r\n")
    return data


KEYS_DICT = {
    "keys": {
        EQ_USER_AUTHENTICATION_RRM_PRIVATE_KEY_KID: {
            "purpose": KEY_PURPOSE_AUTHENTICATION,
            "type": "private",
            "value": get_file_contents("sdc-rrm-authentication-signing-private-v1.pem"),
        },
        SR_USER_AUTHENTICATION_PUBLIC_KEY_KID: {
            "purpose": KEY_PURPOSE_AUTHENTICATION,
            "type": "public",
            "value": get_file_contents(
                "sdc-sr-authentication-encryption-public-v1.pem"
            ),
        },
    }
}


@pytest.fixture(scope='session')
def base_url():
    return 'http://localhost:5000/'

@pytest.fixture(scope="session")
def token_generator():
    key_store = KeyStore(KEYS_DICT)

    return TokenGenerator(
        key_store,
        EQ_USER_AUTHENTICATION_RRM_PRIVATE_KEY_KID,
        SR_USER_AUTHENTICATION_PUBLIC_KEY_KID,
    )


@pytest.fixture
def open_questionnaire(page: Page, token_generator: TokenGenerator):

    def _open_questionnaire(schema_name: str):
        token = token_generator.create_token_v2(
            theme="social", schema_name=schema_name
        )
        url = f"/session?token={token}"
        page.goto(url, wait_until="networkidle")
    
    return _open_questionnaire
