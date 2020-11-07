#!/bin/bash
if [ -d /code/data/ ]; then
    echo "Database seems to already exist."
else
    echo "Creating database..."
    mkdir -p /code/data/
    python app/db_setup.py
fi
