# Stage 1 - Builder
FROM python:3.11-alpine AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --prefix=/install -r requirements.txt

# Stage 2 - Final image
FROM python:3.11-alpine

RUN adduser -D -s /bin/sh appuser

WORKDIR /app

COPY --from=builder /install /usr/local

COPY worker.py .

USER appuser

HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 CMD python -c "import redis; import os; r = redis.Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379, password=os.environ.get('REDIS_PASSWORD')); r.ping()"

CMD ["python", "worker.py"]