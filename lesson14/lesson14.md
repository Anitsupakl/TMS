1. Написать скрипт для поиска свободного порта из диапазона M-N, где M и N - передаются скрипту как аргументы
https://github.com/Anitsupakl/TMS/blob/main/lesson14/check_free_ports.sh 
2. Написать скрипт, для деплоя лендинга https://gitlab.com/dos-26/cmdb/frontend и скрипт для его проверки
https://github.com/Anitsupakl/TMS/blob/main/lesson14/deploy_lending.sh 

3. Развернуть Python-веб-сервер как systemd демон
![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson13/http_service.png?raw=true)

Требования
Сервер запущен как systemd демон с правами пользователя webadmin
Пользователь webadmin не имеет shell-доступпа и является членом группы webgroup
Код сервера расположен в директории /opt/srv/webapp; в той же диреткории лежит content/index.html с содержимым
