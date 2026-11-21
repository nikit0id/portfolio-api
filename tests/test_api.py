import pytest
from fastapi.testclient import TestClient

from app import app, connect


@pytest.fixture()
def client():
    with TestClient(app) as client:
        yield client


def test_health_and_metrics(client):
    assert client.get("/health").json() == {"status": "ok"}
    assert "http_requests_total" in client.get("/metrics").text


def test_task_lifecycle(client):
    created = client.post("/tasks", json={"title": " Test backup "})
    assert created.status_code == 201
    task = created.json()
    try:
        assert task["title"] == "Test backup"
        assert task["done"] is False
        assert task in client.get("/tasks").json()
        changed = client.patch(f"/tasks/{task['id']}", json={"done": True})
        assert changed.json() == {**task, "done": True}
    finally:
        with connect() as db:
            db.execute("DELETE FROM tasks WHERE id = %s", (task["id"],))


def test_validation(client):
    assert client.post("/tasks", json={"title": " "}).status_code == 422
    assert client.patch("/tasks/-1", json={"done": False}).status_code == 404
