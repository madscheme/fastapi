import pytest
from fastapi.testclient import TestClient
from model.user import User
from main import app

client = TestClient(app)

@pytest.fixture
def sample() -> User:
    return User(name="elsa", hash="123")

def test_create(sample):
    resp = client.post("/user", json=sample.dict())
    assert resp.status_code == 201

def test_create_duplicate(sample):
    resp = client.post("/user", json=sample.dict())
    assert resp.status_code == 409

def test_get_one(sample):
    resp = client.get(f"/user/{sample.name}")
    assert resp.json() == sample.dict()

def test_get_one_missing():
    resp = client.get("/user/bobcat")
    assert resp.status_code == 404

def test_modify(sample):
    resp = client.patch(f"/user/{sample.name}", json=sample.dict())
    assert resp.json() == sample.dict()

def test_modify_missing(sample):
    resp = client.patch("/user/dumbledore", json=sample.dict())
    assert resp.status_code == 404

def test_delete(sample):
    resp = client.delete(f"/user/{sample.name}")
    assert resp.json() is None
    assert resp.status_code == 200

def test_delete_missing(sample):
    resp = client.delete(f"/user/{sample.name}")
    assert resp.status_code == 404
