import os
import random

import requests
import yaml
from flask import Flask, request

loadbalancer = Flask(__name__)


def load_configuration(path):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    abs_path = os.path.join(dir_path, path)

    with open(abs_path) as config_file:
        config = yaml.safe_load(config_file)

    return config


config = load_configuration("../loadbalancer.yaml")


@loadbalancer.route("/")
def router():
    host_header = request.headers["Host"]
    for entry in config["hosts"]:
        if host_header == entry["host"]:
            response = requests.get(f'http://{random.choice(entry["servers"])}')
            return response.content, response.status_code
    return "Not Found", 404


@loadbalancer.route("/<path>")
def path_router(path):
    for entry in config["paths"]:
        if ("/" + path) == entry["path"]:
            response = requests.get(f'http://{random.choice(entry["servers"])}')
            return response.content, response.status_code
    return "Not Found", 404
