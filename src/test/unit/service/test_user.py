from fastapi import HTTPException
import pytest
import os
os.environ["CRYPTID_UNIT_TEST"] = "true"
from model.user import User
from web import user

@pytest.fixture
def sample() -> User:
    return User(name="faxfayfaz", hash="ghi")

@pytest.fixture
def fakes() -> list[User]:
    return user.get_all()

def test_create(sample):
    assert user.create(sample) == sample

def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as exc:
        _ = user.create(fakes[0])
        assert exc.value.status_code == 404

def test_get_one(fakes):
    assert user.get_one(fakes[0].name) == fakes[0]

def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        _ = user.get_one("bobcat")
        assert exc.value.status_code == 404
