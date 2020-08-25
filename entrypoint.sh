#!/bin/bash
export PATH=$PATH:/usr/local/bin
export PYTHONPATH=/app

# shellcheck disable=SC2164
cd /app

export TILT_CONFIG="${TILT_CONFIG:-/etc/tilty/tilty.ini}"
[[ ! -f "${TILT_CONFIG}" ]] && (
  # shellcheck disable=SC2046
  mkdir -p $(dirname "${TILT_CONFIG}");
  cat <<EOF >"${TILT_CONFIG}"
[general]
sleep_interval = 30
logging_level = INFO

# This should stay unchanged to make the tilty-dashboard continues to work
[sqlite]
file = /etc/tilty/tilt.sqlite
EOF
)

exec gunicorn --worker-class eventlet -w 1 -c config/gunicorn.py tilty_dashboard:app
