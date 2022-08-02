import pytest
import json
from app import app

def test_token():
    payload = {
        "user_id": "1", 
    }
    result = {
        "signature" : "40085d0a1ccbc4b040effdb97a31f9f6e3aa4bdb53df0cb02578d84f8b4fb0b7",
        "user_id" : "1",
    }
    
    response = app.test_client().post('/token', data=json.dumps(payload))

    assert response.json == result