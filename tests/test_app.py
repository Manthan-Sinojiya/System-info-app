import json
from app import app

def test_index():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert r.get_json() == {"message": "Hello from Demo DevOps App!"}

def test_echo():
    client = app.test_client()
    payload = {"name":"sinojiya"}
    r = client.post("/echo", json=payload)
    assert r.status_code == 201
    assert r.get_json()["you_sent"] == payload
