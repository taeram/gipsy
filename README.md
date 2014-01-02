Gipsy
=====

Gipsy gives you your public IP address as JSON.

Requirements
============
You'll need the following:

* A [Heroku](https://www.heroku.com/) account, if you want to deploy to Heroku.
* [Python 2.7.3](http://www.python.org/)
* [pip](https://github.com/pypa/pip)
* [Virtualenv](https://github.com/pypa/virtualenv)

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
    python server.py
```

Heroku setup:
```bash
    # Clone the repo
    git clone git@github.com:taeram/gipsy.git
    cd ./gipsy

    # Create your Heroku app
    heroku apps:create

    # Set the flask environment
    heroku config:set FLASK_ENV=production

    # Push to Heroku
    git push heroku master
```

Usage
=====

To get your system's IP address:

```bash
curl http://your.herokuapp.com/
```

Response:
```json
{
    "address": "184.71.226.22"
}
```

If you're using JSON in a shell script, you might try [jq](http://stedolan.github.io/jq/)
to simplify parsing the JSON.


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/taeram/gipsy/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

