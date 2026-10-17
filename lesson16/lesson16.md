1. Запустить приложение https://github.com/anestesia001/dos-36-js как systemd-демон
   
https://github.com/Anitsupakl/TMS/blob/main/lesson16/server-json.service

Статус

![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson16/status.png?raw=true)

Запуск

![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson16/system.png?raw=true)

2.Настроить nginx в роли reverse proxy с TLS для этого приложения


 Поднять второй экземпляр приложения из п1 на другом порту
   
   На 3001:
   
![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson16/server2.png?raw=true)


3. Настроить на nginx балансировку запросов (round robin)

upstream backend {

  server 127.0.0.1:3000;
  
  server 127.0.0.1:3001;
  
}

![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson16/curl_balancer.png?raw=true)

Провести нагрузочное тестирование приложения с помощью locust (скрипт с тестами есть в репозитории https://github.com/anestesia001/dos-36-js/blob/main/locustfile.py ; запуск locust -f locustfile.py)
