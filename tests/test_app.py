from api.app import app
from fastapi.testclient import TestClient
from http import HTTPStatus


def test_root_devve_retornar_ola_mundo():
    client = TestClient(app)

    response = client.get("/")

    assert response.json() == {"message": "Olá Mundo!"}
    assert response.status_code == HTTPStatus.OK
