#!/bin/sh
alembic upgrade head
python3 -m flask run --host=0.0.0.0