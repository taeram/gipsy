Gipsy
=====

Gipsy gives you your public IP address as JSON.

Requirements
============
You'll need the following:

* [Docker](https://www.docker.com/)
* [Python 2.7](http://www.python.org/)

Setup
=====
Local development setup:
```bash
    # Clone the repo
    git clone git@github.com:taeram/gipsy.git
    cd ./gipsy

    # Setup and activate virtualenv
    virtualenv .venv
    source ./.venv/bin/activate

    # Install the pip requirements
    pip install -r requirements.txt

    # Start the application
    python main.py
```

Docker setup:
```bash
    docker run --publish 8080:80 taeram/gipsy:latest
```

Usage
=====

To get your system's IP address:

```bash
curl http://localhost:8080/
```

Response:
```json
{
    "address": "184.71.226.22"
}
```

If you're using JSON in a shell script, you might try [jq](http://stedolan.github.io/jq/)
to simplify parsing the JSON.
