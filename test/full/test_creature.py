import pytest
from fastapi.testclient import TestClient
from model.creature import Creature
from main import app

client = TestClient(app)

@pytest.fixture(scope="session")
def sample() -> Creature:
    return Creature(name="Cthulhu",
        description="ichorous",
        country="*", area="*", aka="Ancient One")

def test_create(sample):
    resp = client.post("/creature", json=sample.dict())
    assert resp.status_code == 201

def test_create_duplicate(sample):
    resp = client.post("/creature", json=sample.dict())
    assert resp.status_code == 409

def test_get_one(sample):
    resp = client.get(f"/creature/{sample.name}")
    assert resp.json() == sample.dict()

def test_get_one_missing():
    resp = client.get("/creature/bobcat")
    assert resp.status_code == 404

def test_modify(sample):
    resp = client.patch(f"/creature/{sample.name}", json=sample.dict())
    assert resp.json() == sample.dict()

def test_modify_missing(sample):
    resp = client.patch("/creature/rougarou", json=sample.dict())
    assert resp.status_code == 404

def test_delete(sample):
    resp = client.delete(f"/creature/{sample.name}")
    assert resp.status_code == 200
    assert resp.json() is None

def test_delete_missing(sample):
    resp = client.delete(f"/creature/{sample.name}")
    assert resp.status_code == 404
