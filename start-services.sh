#!/bin/bash
set -x
set -o allexport
# shellcheck disable=SC1091
source .env.docker
set +o allexport

BUILD_PATH="$PWD"
export BUILD_PATH

# check if network exists
# shellcheck disable=SC1091
source .docker.net

docker-compose up --remove-orphans
