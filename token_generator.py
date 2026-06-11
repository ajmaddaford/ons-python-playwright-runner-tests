from copy import deepcopy
from datetime import datetime, timedelta, timezone
from time import time
from uuid import uuid4

from sdc.crypto.encrypter import encrypt


ACCOUNT_SERVICE_URL = "http://upstream.url"

# "version" is excluded here as it is handled independently
TOP_LEVEL_METADATA_KEYS = [
    "tx_id",
    "account_service_url",
    "case_id",
    "collection_exercise_sid",
    "response_id",
    "response_expires_at",
    "language_code",
    "schema_name",
    "schema_url",
    "cir_instrument_id",
    "channel",
    "region_code",
    "roles",
]

TOP_LEVEL_KEYS = TOP_LEVEL_METADATA_KEYS + ["exp", "jti", "iat"]

PAYLOAD_V2 = {
    "version": "v2",
    "survey_metadata": {
        "data": {
            "case_ref": "1000000000000001",
            "user_id": "integration-test",
            "period_id": "201604",
            "ru_name": "Integration Testing",
            "display_address": "68 Abingdon Road, Goathill",
            "qid": str(uuid4()),
        },
        "receipting_keys": ["qid"],
    },
    "collection_exercise_sid": "789",
    "response_id": "1234567890123456",
    "language_code": "en",
    "roles": [],
    "account_service_url": ACCOUNT_SERVICE_URL,
}


def populate_with_extra_payload_items(key, value, payload):
    payload[key] = value

def get_response_expires_at() -> str:
    return (datetime.now(tz=timezone.utc) + timedelta(days=1)).isoformat()


class TokenGenerator:
    def __init__(self, key_store, upstream_kid, sr_public_kid):
        self._key_store = key_store
        self._upstream_kid = upstream_kid
        self._sr_public_kid = sr_public_kid

    @staticmethod
    def _get_payload_with_params(
        *,
        schema_name=None,
        schema_url=None,
        cir_instrument_id=None,
        payload=None,
        **extra_payload,
    ):
        if payload is None:
            payload = PAYLOAD_V2
        payload_vars = deepcopy(payload)
        payload_vars["tx_id"] = str(uuid4())
        if schema_name:
            payload_vars["schema_name"] = schema_name
        if schema_url:
            payload_vars["schema_url"] = schema_url
        if cir_instrument_id:
            payload_vars["cir_instrument_id"] = cir_instrument_id

        payload_vars["iat"] = time()
        payload_vars["exp"] = payload_vars["iat"] + float(3600)  # one hour from now
        payload_vars["jti"] = str(uuid4())
        payload_vars["case_id"] = str(uuid4())
        payload_vars["response_expires_at"] = get_response_expires_at()

        for key, value in extra_payload.items():
            if key in TOP_LEVEL_KEYS:
                populate_with_extra_payload_items(key, value, payload_vars)
            else:
                populate_with_extra_payload_items(
                    key, value, payload_vars["survey_metadata"]["data"]
                )

        return payload_vars

    def create_token_v2(self, schema_name, theme="default", **extra_payload):
        payload_for_theme = PAYLOAD_V2
        payload = self._get_payload_with_params(
            schema_name=schema_name, payload=payload_for_theme, **extra_payload
        )

        return self.generate_token(payload)

    def create_token_with_schema_url(self, schema_url, **extra_payload):
        payload_vars = self._get_payload_with_params(
            schema_url=schema_url, **extra_payload
        )

        return self.generate_token(payload_vars)

    def generate_token(self, payload):
        return encrypt(payload, self._key_store, "authentication")
