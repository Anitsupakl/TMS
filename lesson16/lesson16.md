1. Запустить приложение https://github.com/anestesia001/dos-36-js как systemd-демон
   
https://github.com/Anitsupakl/TMS/blob/main/lesson16/server-json.service

Статус

![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson16/status.png?raw=true)

Запуск

![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson16/system.png?raw=true)

2.Настроить nginx в роли reverse proxy с TLS для этого приложения   
`
upstream backend {
  server 127.0.0.1:3000;
  server 127.0.0.1:3001;
}

server {
  listen 80;
  server_name 192.168.211.12; 
  return 301 https://$host$request_uri;
}

server {
  listen 443 ssl;
  server_name 192.168.211.12;
   
  ssl_certificate /etc/nginx/ssl/server_js.crt;
  ssl_certificate_key /etc/nginx/ssl/server_js.key;
  ssl_protocols TLSv1.2 TLSv1.3;
  ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
  ssl_prefer_server_ciphers off;
  add_header Strict-Transport-Security max-age=312536000;


  access_log /var/log/nginx/server_json_access.log custom;
  error_log /var/log/nginx/server_json_error.log;
  
  root /var/www/static/;
   
  location / {
    proxy_pass http://backend;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  }
 
}
`   

3.Поднять второй экземпляр приложения из п1 на другом порту
   
   На 3001:
   
![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson16/server2.png?raw=true)


4. Настроить на nginx балансировку запросов (round robin)

upstream backend {

  server 127.0.0.1:3000;
  
  server 127.0.0.1:3001;
  
}

![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson16/curl_balancer.png?raw=true)

5. Провести нагрузочное тестирование приложения с помощью locust (скрипт с тестами есть в репозитории https://github.com/anestesia001/dos-36-js/blob/main/locustfile.py ; запуск locust -f locustfile.py)
