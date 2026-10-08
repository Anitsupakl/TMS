1. Написать скрипт для поиска свободного порта из диапазона M-N, где M и N - передаются скрипту как аргументы
   Предупреждение! Скрипт содержит извращения,при просмотре может стать больно
   
https://github.com/Anitsupakl/TMS/blob/main/lesson14/check_free_ports.sh

3. Написать скрипт, для деплоя лендинга https://gitlab.com/dos-26/cmdb/frontend и скрипт для его проверки
https://github.com/Anitsupakl/TMS/blob/main/lesson14/deploy_lending.sh 

4. Развернуть Python-веб-сервер как systemd демон
![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson14/status.png)

8000 у меня занят, поэтому я нагло изменила на 9000
![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson14/localhost.png)

Требования

Сервер запущен как systemd демон с правами пользователя webadmin
Дублирую 3 пункт с картинкой

Пользователь webadmin не имеет shell-доступпа и является членом группы webgroup
![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson14/no_shell_for_user.png)
![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson14/group.png)

Код сервера расположен в директории /opt/srv/webapp; в той же диреткории лежит content/index.html с содержимым
![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson14/treewebapp.png)
