#Установить nginx (sudo apt install -y nginx) и написать скрипт для мониторинга состояния демона nginx (systemctl status) с и автоматическим перезапуском (systemctl restart), если он не запущен

#!/bin/bash
NGINX='nginx'
CHECK_EXIST_NGINX=$( ps aux | grep nginx | grep "worker process")
NGINX_STATUS=$(  systemctl status nginx )
NGINX_INSTALL=$( sudo apt install -y nginx)
#CHECK_INACTIVE_NGINX=$( ps aux | grep nginx | grep "inactive")
#RESTART_NGINX= $( systemctl restart nginx )

if [ ! CHECK_EXIST_NGINX ]; then
  ${NGINX_INSTALL}
fi

if systemctl is-active ${NGINX}; then 
  echo "Нджинкс активен"

else
  echo -e "Сервис не запущен, запускаю рестарт"
  $( systemctl restart nginx)
  echo "Подождите cекунду"
    sleep 1
  echo 
  echo ${NGINX_STATUS}
fi

