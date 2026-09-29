#Написать скрипт для мониторинга доступности хоста (можно использовать ping) с записью результата в лог с датой и временем (формат произвольный).

#!/bin/bash

AVALIABLE_HOST=$(ping -c 1 "$1")

echo -e "${AVALIABLE_HOST}/n"

LOG_FILE="${AVALIABLE_HOST}+ $(date '+%Y-%m-%d')"

echo
echo ${LOG_FILE} > log_$(date '+%Y-%m-%d')
