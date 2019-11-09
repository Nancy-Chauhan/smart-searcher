#!/bin/sh

if [ "dev" = "$1" ]
then
    echo 'Starting development server...'
    python3 -m smartsearcher.server
else
    gunicorn --bind 0.0.0.0:5000 smartsearcher.server:app
fi
