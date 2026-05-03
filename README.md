# HNG Stage 2 - Containerized Microservices

A job processing system built with FastAPI, Node.js, Redis and Docker.

## Architecture

Frontend (Node.js) → API (FastAPI) → Redis → Worker (Python)

## Prerequisites

- Docker Desktop installed
- Docker Compose installed
- Git installed

## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/LORDS-001/hng14-stage2-devops.git
cd hng14-stage2-devops
```

### 2. Create your .env file
```bash
cp .env.example .env
```
Edit `.env` and set your values:

REDIS_PASSWORD=yourpassword
APP_ENV=production

### 3. Start the full stack
```bash
docker compose up --build
```

### 4. Verify all services are healthy
```bash
docker compose ps
```

Expected output:

NAME                             STATUS
hng14-stage2-devops-redis-1      Up (healthy)
hng14-stage2-devops-api-1        Up (healthy)
hng14-stage2-devops-worker-1     Up (healthy)
hng14-stage2-devops-frontend-1   Up (healthy)

### 5. Open the app
Visit http://localhost:3000 in your browser.
Click "Submit New Job" and watch the status change from queued to completed.

## Services

| Service | Language | Port | Description |
|---|---|---|---|
| frontend | Node.js/Express | 3000 | Web UI for submitting jobs |
| api | Python/FastAPI | 8000 (internal) | Creates jobs and serves status |
| worker | Python | - | Processes jobs from Redis queue |
| redis | Redis 7 | 6379 (internal) | Job queue and status store |

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/jobs` | POST | Create a new job |
| `/jobs/{job_id}` | GET | Get job status |

## CI/CD Pipeline

The GitHub Actions pipeline runs in strict order:

lint → test → build → security scan → integration test → deploy

- **Lint:** flake8 (Python), eslint (JavaScript), hadolint (Dockerfiles)
- **Test:** pytest with Redis mocked, coverage report uploaded as artifact
- **Build:** Docker images built and pushed to local registry
- **Security:** Trivy scan on all images, results uploaded as SARIF artifact
- **Integration:** Full stack brought up, job submitted and verified complete
- **Deploy:** Rolling update on EC2 server with health check verification

## Environment Variables

| Variable | Description |
|---|---|
| `REDIS_PASSWORD` | Password for Redis authentication |
| `REDIS_HOST` | Redis hostname (default: redis) |
| `APP_ENV` | Application environment |
| `API_URL` | URL for frontend to reach API |

## Bugs Fixed

See [FIXES.md](FIXES.md) for a full list of all bugs found and fixed.