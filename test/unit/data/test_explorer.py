import os
import pytest
from model.explorer import Explorer
from error import Missing, Duplicate

# -set this before data imports below call data.init
os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import explorer

@pytest.fixture
def sample() -> Explorer:
    return Explorer(name="Pa Tuohy",
        description="Expectorating explorer",
        country="IE")

def test_create(sample):
    resp = explorer.create(sample)
    assert resp == sample

def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = explorer.create(sample)

def test_get_exists(sample):
    resp = explorer.get_one(sample.name)
    assert resp == sample
    
def test_get_missing():
    with pytest.raises(Missing):
        _ = explorer.get_one("Sam Gamgee")

def test_modify(sample):
    sample.country = "CA"
    resp = explorer.modify(sample.name, sample)
    assert resp == sample

def test_modify_missing():
    bob: Explorer = Explorer(name="Bob", description="Bob who?",
        country="BE")
    with pytest.raises(Missing):
        _ = explorer.modify(bob.name, bob)

def test_delete(sample):
    resp = explorer.delete(sample.name)
    assert resp is None

def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = explorer.delete(sample.name)
