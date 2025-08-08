import sys
from pathlib import Path

# Add project root to sys.path before any imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app  # noqa: E402


def test_index():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert r.get_json() == {"message": "Hello from Demo DevOps App!"}


def test_echo():
    client = app.test_client()
    payload = {"name": "sinojiya"}
    r = client.post("/echo", json=payload)
    assert r.status_code == 201
    assert r.get_json()["I'm Manthan."] == payload
