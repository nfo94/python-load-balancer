import pytest
from python_load_balancer import loadbalancer


@pytest.fixture
def client():
    with loadbalancer.test_client() as client:
        yield client


def test_hello(client):
    response = client.get("/")
    assert response.data == b"Hello, World!"
