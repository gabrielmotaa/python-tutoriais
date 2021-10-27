#!/usr/bin/env bash
set -x
python3 -m black .
python3 -m isort .
python3 -m flake8 snps_util tests
python3 -m pytest