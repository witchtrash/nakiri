#!/bin/sh

cd /app
pipenv run flask db init --yes
pipenv run flask run --host=0.0.0.0