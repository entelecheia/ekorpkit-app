#!/bin/bash
set -x
set -o allexport
source backend/.env
source frontend/.env
set +o allexport

docker-compose up -d --remove-orphans
  # --env-file backend/.env \
  # --env-file frontend/.env \
