from fastapi import HTTPException
import pytest
import os
os.environ["CRYPTID_UNIT_TEST"] = "true"
from model.user import User
from web import user
from error import Missing, Duplicate

@pytest.fixture
def sample() -> User:
    return User(name="Pa Tuohy", hash="...")

@pytest.fixture
def fakes() -> list[User]:
    return user.get_all()

def assert_duplicate(exc):
    assert exc.value.status_code == 404
    assert "Duplicate" in exc.value.msg

def assert_missing(exc):
    assert exc.value.status_code == 404
    assert "Missing" in exc.value.msg

def test_create(sample):
    assert user.create(sample) == sample

def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as exc:
        resp = user.create(fakes[0])
        assert_duplicate(exc)

def test_get_one(fakes):
    assert user.get_one(fakes[0].name) == fakes[0]

def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        resp = user.get_one("Buffy")
        assert_missing(exc)

def test_modify(fakes):
    assert user.modify(fakes[0].name, fakes[0]) == fakes[0]

def test_modify_missing(sample):
    with pytest.raises(HTTPException) as exc:
        resp = user.modify(sample.name, sample)
        assert_missing(exc)

def test_delete(fakes):
    assert user.delete(fakes[0].name) is None

def test_delete_missing(sample):
    with pytest.raises(HTTPException) as exc:
        resp = user.delete("Wally")
        assert_missing(exc)
