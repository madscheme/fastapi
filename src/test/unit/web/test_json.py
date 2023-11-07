import datetime
import pytest
from fastapi.encoders import jsonable_encoder
import json 

@pytest.fixture
def data():
    return datetime.datetime.now()

def test_json_dump(data):
    with pytest.raises(Exception):
        json_out = json.dumps(data)

def test_encoder(data):
    out = jsonable_encoder(data)
    assert out
    print(out, type(out))
    json_out = json.dumps(out)
    assert json_out
    print(json_out)
