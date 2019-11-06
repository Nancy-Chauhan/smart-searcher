#!/bin/sh

if [ $1 == "dev" ]
then
    echo 'Starting development server...'
    python3 -m smartsearcher.server
else
    gunicorn --bind 0.0.0.0:5000 smartsearcher:app
fi
