#!/usr/bin/env bash

echo "$(tput setaf 1)Building docker images ...$(tput sgr0)"
docker build -t web -t web:latest .
docker build -t nginx .docker/nginx
docker build -t prometheus .docker/prometheus
docker build -t grafana .docker/grafana
docker build -t logstash .docker/logstash
docker build -t kibana .docker/kibana
