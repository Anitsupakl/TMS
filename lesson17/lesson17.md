1. Запустить приложение https://github.com/anestesia001/carss/tree/main как systemd демон

![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson17/status.png)
![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson17/curl.png)

Записи в бд после запуска
![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson17/dt.png)


2.Настроить nginx как reverse proxy для этого приложения
```python
server {
  listen 80;
  server_name 192.168.211.12;
  access_log /var/log/nginx/database_access.log custom;
  error_log /var/log/nginx/database_error.log;

location / {
    proxy_pass http://127.0.0.1:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  }
}
```
3.Написать скрипт для бэкапов БД приложения
https://github.com/Anitsupakl/TMS/blob/main/lesson17/backup.sh 

![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson17/dump.png)

