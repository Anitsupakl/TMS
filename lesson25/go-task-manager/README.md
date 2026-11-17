# Task Manager API

REST API для управления задачами, написанный на Go с использованием PostgreSQL.

## Технологии

- Go 1.24
- PostgreSQL 17


## Быстрый запуск

**1. Клонировать или скачать проект**

Перейти в каталог проекта:

```bash
cd go-task-api
```

**2. Настроить переменные окружения**

```bash
cp .env.example .env
```

Изменить пароль PostgreSQL в `.env`.

**3. Подготовить Go-зависимости**

При первом создании проекта выполнить:

```bash
go mod tidy
```

Команда сформирует файл `go.sum`.

**4. Собрать приложение*

```bash
CGO_ENABLED=0 GOOS=linux \
    go build -trimpath -ldflags="-s -w" -o server .
```


## Проверка API

```bash
curl http://localhost:8080/health
```

Ожидаемый ответ:

```json
{
  "status": "ok"
}
```

## API

### Получение всех задач

```bash
curl http://localhost:8080/tasks
```

### Получение задачи по ID

```bash
curl http://localhost:8080/tasks/1
```

### Создание задачи

```bash
curl -X POST http://localhost:8080/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Настроить CI/CD",
    "description": "Создать pipeline в GitLab",
    "completed": false
  }'
```

### Обновление задачи

Метод PUT заменяет редактируемые поля задачи.

```bash
curl -X PUT http://localhost:8080/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Настроить CI/CD",
    "description": "Pipeline готов",
    "completed": true
  }'
```

### Удаление задачи

```bash
curl -X DELETE http://localhost:8080/tasks/1
```

При успешном удалении возвращается HTTP 204.


## Хранение данных

SQL-скрипт `db/init.sql` выполняется только при первоначальной инициализации пустого каталога данных PostgreSQL.

