from fastapi import HTTPException
import pytest
import os
os.environ["CRYPTID_UNIT_TEST"] = "true"
from model.explorer import Explorer
from web import explorer

@pytest.fixture
def sample() -> Explorer:
    return Explorer(name="Pa Tuohy",
        description="The old sod",
        country="IE")

@pytest.fixture
def fakes() -> list[Explorer]:
    return explorer.get_all()

def assert_duplicate(exc):
    assert exc.value.status_code == 404
    assert "Duplicate" in exc.value.msg

def assert_missing(exc):
    assert exc.value.status_code == 404
    assert "Missing" in exc.value.msg

def test_create(sample):
    assert explorer.create(sample) == sample

def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as exc:
        _ = explorer.create(fakes[0])
        assert_duplicate(exc)

def test_get_one(fakes):
    assert explorer.get_one(fakes[0].name) == fakes[0]

def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        _ = explorer.get_one("bobcat")
        assert_missing(exc)

def test_modify(fakes):
    assert explorer.modify(fakes[0].name, fakes[0]) == fakes[0]

def test_modify_missing(sample):
    with pytest.raises(HTTPException) as exc:
        _ = explorer.modify(sample.name, sample)
        assert_missing(exc)

def test_delete(fakes):
    assert explorer.delete(fakes[0].name) is None

def test_delete_missing(sample):
    with pytest.raises(HTTPException) as exc:
        _ = explorer.delete("emu")
        assert_missing(exc)
