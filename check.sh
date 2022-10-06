#!/usr/bin/env sh

set -o errexit
set -o nounset

pyclean() {
  # Cleaning cache:
  find . |
    grep -E '(__pycache__|\.hypothesis|\.perm|\.cache|\.static|\.py[cod]$)' |
    xargs rm -rf
}

run_checks() {
  echo '[Check Started]'
  set -x # we want to print commands during the CI process.

  # Running linting for all python files in the project:
  python -m flake8

  # Running type checking, see https://github.com/typeddjango/django-stubs
  python -m mypy leeteasy tests

  # Running tests:
  python -m pytest

  # Checking dependencies status:
  python -m pip check

  set +x
  echo '[checks completed]'
}

# Remove any cache before the script:
pyclean

# Clean everything up:
trap pyclean EXIT INT TERM

# Run the CI process:
run_checks
