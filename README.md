### python-load-balancer

This project uses [Flask](https://flask.palletsprojects.com/en/3.0.x/),
[Poetry](https://python-poetry.org/), and [Ruff](https://docs.astral.sh/ruff/). This is a study codebase.
To use this code clone this repository:

```bash
git clone git@github.com:nfo94/python-load-balancer.git
```

Enter the project folder with `cd python-load-balancer`. Then build the image locally:

```bash
make build
```

to compose the services:

```bash
make compose
```

The `app.py` file is our main server and the `loadbalancer.py` file is our load balancer, meaning
is the software that will handle the requests for the instances created from the image of the `app.py`
file (mangos and apples).

You can check other useful commands in the Makefile.
