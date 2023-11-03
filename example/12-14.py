import os
os.environ["CRYPTID_UNIT_TEST"]= "true"
import pytest

from model.creature import Creature
from error import Missing, Duplicate

@pytest.fixture
def sample() -> Creature:
    return Creature(name="yeti",
        description="Abominable Snowman",
        country="CN",
        area="Himalayas",
        description="Handsome Himalayan")

def test_create(sample):
    resp = data.create(sample)
    assert resp == sample

def test_create_duplicate(data):
    resp = data.create(data)
    assert resp == data
    with pytest.raises(Duplicate):
        resp = service.create(data)

def test_get_exists(data):
    resp = data.create(data)
    assert resp == data
    resp = data.get_one(data.name)
    assert resp == data

def test_get_missing():
    with pytest.raises(Missing):
        resp = data.get_one("boxturtle")

def test_modify(data):
    data.country = "CA" # Canada!
    resp = data.modify(data.name, data)
    assert resp == data

def test_modify_missing():
    bob: Creature = Creature(name="bob",
        description="some guy", country="??")
    with pytest.raises(Missing):
        resp = data.modify(bob.name, bob)
