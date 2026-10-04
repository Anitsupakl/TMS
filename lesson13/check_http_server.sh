#!/bin/bash

HOST="127.0.0.1"
PORT=8080
ENDPOINT_HEALTH=$(curl -s http://127.0.0.1:8080/health)
DAEMON_STATUS=$(systemctl status http-server.service | grep 'Active:' | awk '{print $2, $3}')

echo "Статус демона:"
echo "$DAEMON_STATUS"
echo
echo "Доступность порта:"
echo "$(nc -vz $HOST $PORT)"
echo
echo "Ответ эндпоинта /health:"
echo "$ENDPOINT_HEALTH"


