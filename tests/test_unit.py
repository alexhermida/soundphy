import json

import pytest


def decode(response):
    """
    Decode an HTTP response with JSON content.
    """
    return json.loads(response.content.decode('utf'))


@pytest.mark.django_db
def test_sounds_empty_database(client):
    """
    Listing sounds from an empty database should result in an empty list.
    Any client can make this request (no authentication needed).
    """
    response = client.get('/sounds/')
    assert response.status_code == 200
    assert decode(response) == []
