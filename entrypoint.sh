#!/bin/sh
export PATH=$PATH:/usr/local/bin
export PYTHONPATH=/app

# shellcheck disable=SC2164
cd /app

exec gunicorn --worker-class eventlet -w 1 -c config/gunicorn.py tilty_dashboard:app
