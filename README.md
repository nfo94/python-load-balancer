### python-load-balancer

This project uses [Flask](https://flask.palletsprojects.com/en/3.0.x/),
[Poetry](https://python-poetry.org/), and [Ruff](https://docs.astral.sh/ruff/). To use this code
clone this repository:

```bash
git clone git@github.com:nfo94/python-load-balancer.git
```

Enter the project folder with `cd python-load-balancer`. Then build the image locally:

```bash
docker build -t python-load-balancer
```

Run the image locally:

```bash
docker run -p 5000:5000 python-load-balancer
```

To format code:

```bash
make lint.format
```

You can check other useful commands in the Makefile.
