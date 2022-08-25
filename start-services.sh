#!/bin/bash
set -x
set -o allexport
source backend/.env
source frontend/.env
set +o allexport

docker-compose up --remove-orphans
