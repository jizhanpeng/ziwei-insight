from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["name"] == "ziwei-insight"


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "ziwei-insight",
    }


def test_hello_default_language() -> None:
    response = client.get("/hello/张三")

    assert response.status_code == 200
    assert response.json() == {"message": "你好，张三"}


def test_hello_english() -> None:
    response = client.get("/hello/张三", params={"lang": "en"})

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, 张三"}
