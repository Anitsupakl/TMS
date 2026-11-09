FROM python:3.12-slim
LABEL maintainer="kapustina"
LABEL description="Python app"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1 \
    REDIS_HOST=127.0.0.1
    
WORKDIR /app
RUN groupadd --system appgroup && \
    useradd --system --gid appgroup --create-home appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=appuser:appgroup app.py .
USER appuser
EXPOSE 5000
CMD ["python", "app.py"]

