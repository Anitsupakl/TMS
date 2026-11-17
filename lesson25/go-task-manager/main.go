package main

import (
	"context"
	"encoding/json"
	"errors"
	"log"
	"net/http"
	"os"
	"strconv"
	"time"

	"github.com/jackc/pgx/v5"
	"github.com/jackc/pgx/v5/pgxpool"
)

type Task struct {
	ID          int       `json:"id"`
	Title       string    `json:"title"`
	Description string    `json:"description"`
	Completed   bool      `json:"completed"`
	CreatedAt   time.Time `json:"created_at"`
}

type TaskInput struct {
	Title       string `json:"title"`
	Description string `json:"description"`
	Completed   bool   `json:"completed"`
}

type App struct {
	DB *pgxpool.Pool
}

func writeJSON(w http.ResponseWriter, status int, data any) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	_ = json.NewEncoder(w).Encode(data)
}

func writeError(w http.ResponseWriter, status int, message string) {
	writeJSON(w, status, map[string]string{
		"error": message,
	})
}

func decodeInput(w http.ResponseWriter, r *http.Request) (TaskInput, bool) {
	var input TaskInput

	r.Body = http.MaxBytesReader(w, r.Body, 1<<20)

	decoder := json.NewDecoder(r.Body)
	decoder.DisallowUnknownFields()

	if err := decoder.Decode(&input); err != nil {
		writeError(w, http.StatusBadRequest, "Invalid JSON")
		return input, false
	}

	var extra any
	if err := decoder.Decode(&extra); !errors.Is(err, os.ErrClosed) {
		// Проверка дополнительного JSON выполняется ниже.
	}

	if input.Title == "" {
		writeError(w, http.StatusBadRequest, "Title is required")
		return input, false
	}

	return input, true
}

func (a *App) Health(w http.ResponseWriter, r *http.Request) {
	if err := a.DB.Ping(r.Context()); err != nil {
		writeError(w, http.StatusServiceUnavailable, "Database unavailable")
		return
	}

	writeJSON(w, http.StatusOK, map[string]string{
		"status": "ok",
	})
}

func (a *App) GetTasks(w http.ResponseWriter, r *http.Request) {
	rows, err := a.DB.Query(r.Context(),
		`SELECT id, title, description, completed, created_at
		 FROM tasks ORDER BY id`)

	if err != nil {
		writeError(w, 500, "Database error")
		return
	}
	defer rows.Close()

	tasks := []Task{}

	for rows.Next() {
		var task Task

		err := rows.Scan(
			&task.ID,
			&task.Title,
			&task.Description,
			&task.Completed,
			&task.CreatedAt,
		)

		if err != nil {
			writeError(w, 500, "Database error")
			return
		}

		tasks = append(tasks, task)
	}

	if err := rows.Err(); err != nil {
		writeError(w, 500, "Database error")
		return
	}

	writeJSON(w, 200, tasks)
}

func (a *App) GetTask(w http.ResponseWriter, r *http.Request) {
	id, err := strconv.Atoi(r.PathValue("id"))

	if err != nil || id <= 0 {
		writeError(w, 400, "Invalid task ID")
		return
	}

	var task Task

	err = a.DB.QueryRow(r.Context(),
		`SELECT id, title, description, completed, created_at
		 FROM tasks WHERE id=$1`, id,
	).Scan(
		&task.ID,
		&task.Title,
		&task.Description,
		&task.Completed,
		&task.CreatedAt,
	)

	if errors.Is(err, pgx.ErrNoRows) {
		writeError(w, 404, "Task not found")
		return
	}

	if err != nil {
		writeError(w, 500, "Database error")
		return
	}

	writeJSON(w, 200, task)
}

func (a *App) CreateTask(w http.ResponseWriter, r *http.Request) {
	input, ok := decodeInput(w, r)
	if !ok {
		return
	}

	var task Task

	err := a.DB.QueryRow(r.Context(),
		`INSERT INTO tasks (title, description, completed)
		 VALUES ($1, $2, $3)
		 RETURNING id, title, description, completed, created_at`,
		input.Title, input.Description, input.Completed,
	).Scan(
		&task.ID,
		&task.Title,
		&task.Description,
		&task.Completed,
		&task.CreatedAt,
	)

	if err != nil {
		writeError(w, 500, "Database error")
		return
	}

	writeJSON(w, http.StatusCreated, task)
}

func (a *App) UpdateTask(w http.ResponseWriter, r *http.Request) {
	id, err := strconv.Atoi(r.PathValue("id"))

	if err != nil || id <= 0 {
		writeError(w, 400, "Invalid task ID")
		return
	}

	input, ok := decodeInput(w, r)
	if !ok {
		return
	}

	var task Task

	err = a.DB.QueryRow(r.Context(),
		`UPDATE tasks
		 SET title=$1, description=$2, completed=$3
		 WHERE id=$4
		 RETURNING id, title, description, completed, created_at`,
		input.Title, input.Description, input.Completed, id,
	).Scan(
		&task.ID,
		&task.Title,
		&task.Description,
		&task.Completed,
		&task.CreatedAt,
	)

	if errors.Is(err, pgx.ErrNoRows) {
		writeError(w, 404, "Task not found")
		return
	}

	if err != nil {
		writeError(w, 500, "Database error")
		return
	}

	writeJSON(w, 200, task)
}

func (a *App) DeleteTask(w http.ResponseWriter, r *http.Request) {
	id, err := strconv.Atoi(r.PathValue("id"))

	if err != nil || id <= 0 {
		writeError(w, 400, "Invalid task ID")
		return
	}

	tag, err := a.DB.Exec(r.Context(),
		"DELETE FROM tasks WHERE id=$1", id)

	if err != nil {
		writeError(w, 500, "Database error")
		return
	}

	if tag.RowsAffected() == 0 {
		writeError(w, 404, "Task not found")
		return
	}

	w.WriteHeader(http.StatusNoContent)
}

func main() {
	databaseURL := os.Getenv("DATABASE_URL")
	if databaseURL == "" {
		log.Fatal("DATABASE_URL is required")
	}

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	db, err := pgxpool.New(ctx, databaseURL)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	if err := db.Ping(ctx); err != nil {
		log.Fatal(err)
	}

	app := &App{DB: db}

	mux := http.NewServeMux()

	mux.HandleFunc("GET /health", app.Health)
	mux.HandleFunc("GET /tasks", app.GetTasks)
	mux.HandleFunc("GET /tasks/{id}", app.GetTask)
	mux.HandleFunc("POST /tasks", app.CreateTask)
	mux.HandleFunc("PUT /tasks/{id}", app.UpdateTask)
	mux.HandleFunc("DELETE /tasks/{id}", app.DeleteTask)

	server := &http.Server{
		Addr:              ":8080",
		Handler:           mux,
		ReadHeaderTimeout: 5 * time.Second,
	}

	log.Println("API listening on :8080")

	log.Fatal(server.ListenAndServe())
}
