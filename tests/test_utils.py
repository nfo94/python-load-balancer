import yaml

from python_load_balancer.models import Server
from python_load_balancer.utils import (
    get_healthy_server,
    healthcheck,
    transform_backends_from_config,
)


def test_transform_backends_from_config():
    input = yaml.safe_load("""
        hosts:
          - host: www.mango.com
            servers:
              - localhost:8081
              - localhost:8082
          - host: www.apple.com
            servers:
              - localhost:9081
              - localhost:9082
        paths:
          - path: /mango
            servers:
              - localhost:8081
              - localhost:8082
          - path: /apple
            servers:
              - localhost:9081
              - localhost:9082
    """)
    output = transform_backends_from_config(input)
    assert list(output.keys()) == ["www.mango.com", "www.apple.com", "/mango", "/apple"]
    assert output["www.mango.com"][0] == Server("localhost:8081")
    assert output["www.mango.com"][1] == Server("localhost:8082")
    assert output["www.apple.com"][0] == Server("localhost:9081")
    assert output["www.apple.com"][1] == Server("localhost:9082")
    assert output["/mango"][0] == Server("localhost:8081")
    assert output["/mango"][1] == Server("localhost:8082")
    assert output["/apple"][0] == Server("localhost:9081")
    assert output["/apple"][1] == Server("localhost:9082")


def test_get_healthy_server():
    healthy_server = Server("localhost:8081")
    unhealthy_server = Server("localhost:8082")
    unhealthy_server.healthy = False
    register = {
        "www.mango.com": [healthy_server, unhealthy_server],
        "www.apple.com": [healthy_server, healthy_server],
        "www.orange.com": [unhealthy_server, unhealthy_server],
        "/mango": [healthy_server, unhealthy_server],
        "/apple": [unhealthy_server, unhealthy_server],
    }

    assert get_healthy_server("www.mango.com", register) == healthy_server
    assert get_healthy_server("www.apple.com", register) == healthy_server
    assert get_healthy_server("www.orange.com", register) is None
    assert get_healthy_server("/mango", register) == healthy_server
    assert get_healthy_server("/apple", register) is None


def test_healthcheck():
    config = yaml.safe_load("""
        hosts:
          - host: www.mango.com
            servers:
              - localhost:8081
              - localhost:8888
          - host: www.apple.com
            servers:
              - localhost:9081
              - localhost:4444
    """)

    register = healthcheck(transform_backends_from_config(config))
    assert register["www.apple.com"][0].healthy
    assert not register["www.apple.com"][1].healthy
    assert register["www.mango.com"][0].healthy
    assert not register["www.mango.com"][1].healthy
