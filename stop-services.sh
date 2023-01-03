#!/bin/bash
set -x
set -o allexport
# shellcheck disable=SC1091
source .env.docker
set +o allexport

BUILD_PATH="$PWD"
export BUILD_PATH

docker-compose stop && docker-compose rm -f
