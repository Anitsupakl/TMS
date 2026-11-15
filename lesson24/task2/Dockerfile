FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1 

WORKDIR /app
COPY ./python-app_02/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./python-app_02/app.py .
CMD ["python", "app.py"]
