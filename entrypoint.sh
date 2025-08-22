#!/bin/sh
set -x

echo 'Applying migrations...'
alembic upgrade head

echo 'Running server...'
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload