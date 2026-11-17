FROM python:3.12-slim
WORKDIR /app
ARG SERVICE
COPY ${SERVICE}/main.py .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
