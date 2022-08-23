#!/bin/bash
set -x
set -o allexport
source backend/.env
source frontend/.env
set +o allexport

docker-compose stop && docker-compose rm -f
