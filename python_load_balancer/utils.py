import os
import random

import yaml

from python_load_balancer.models import Server


def load_configuration(path):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    abs_path = os.path.join(dir_path, path)

    with open(abs_path) as config_file:
        config = yaml.safe_load(config_file)

    return config


def transform_backends_from_config(config):
    register = {}
    for entry in config.get("hosts", []):
        register.update(
            {entry["host"]: [Server(endpoint) for endpoint in entry["servers"]]}
        )
    for entry in config.get("paths", []):
        register.update(
            {entry["path"]: [Server(endpoint) for endpoint in entry["servers"]]}
        )
    return register


def get_healthy_server(host, register):
    try:
        return random.choice([server for server in register[host] if server.healthy])
    except IndexError:
        return None


def healthcheck(register):
    for host in register:
        for server in register[host]:
            server.healthcheck_and_update_status()
    return register
