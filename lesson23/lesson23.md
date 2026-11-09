Задание 1
Запустить с помощью docker compose приложения 
https://gitlab.com/dos-29-onl/docker-apps/-/tree/main/compose-apps/nodejs-app_01?ref_type=heads

docker compose
```python
services:
  flask-app:
    build: .
    container_name: flask-app
    environment:
      REDIS_HOST: redis
    ports:
     - 5000:5000
    restart: always
    volumes:
      - ./app.py:/app/app.py
  redis:
    image: redis
    container_name: redis_flask
    restart: always
    ports:
      - 6379:6379
```

CURL

![Image Alt](https://github.com/Anitsupakl/TMS/blob/main/lesson23/task1/Screenshot_2026-11-09_20-37-27.png?raw=true)



Задание 2
Запустить с помощью docker compose приложения  https://gitlab.com/dos-29-onl/docker-apps/-/tree/main/compose-apps/python-app_01?ref_type=heads

```python
Dockerfile https://github.com/Anitsupakl/TMS/blob/main/lesson23/task2/Dockerfile
docker compose https://github.com/Anitsupakl/TMS/blob/main/lesson23/task2/docker-compose.yaml
```



