#!/usr/bin/env sh

python main.py
# gunicorn -w 4 -b 127.0.0.1:8080 main:app
