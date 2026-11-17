CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    completed BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

INSERT INTO tasks (title, description, completed)
VALUES
    ('Изучить Go', 'Разобраться с REST API', false),
    ('Изучить Docker', 'Собрать Docker image', false),
    ('Изучить PostgreSQL', 'Научиться работать с SQL', true);
