# FIXES.md — Bug Documentation

## Bug 1
- **File:** `worker/worker.py`
- **Line:** 13
- **Problem:** Used undefined variable `job_id` instead of `job[1]`
- **Fix:** Changed `process_job(job_id.decode())` to `process_job(job[1].decode())`

## Bug 2
- **File:** `worker/worker.py`
- **Line:** 5
- **Problem:** Hardcoded `localhost` as Redis host — fails inside Docker containers
- **Fix:** Changed to `host=os.environ.get("REDIS_HOST", "redis")`

## Bug 3
- **File:** `worker/worker.py`
- **Line:** 5
- **Problem:** No Redis password provided despite Redis requiring authentication
- **Fix:** Added `password=os.environ.get("REDIS_PASSWORD")`

## Bug 4
- **File:** `api/main.py`
- **Line:** 9
- **Problem:** Hardcoded `localhost` as Redis host — fails inside Docker containers
- **Fix:** Changed to `host=os.environ.get("REDIS_HOST", "redis")`

## Bug 5
- **File:** `api/main.py`
- **Line:** 9
- **Problem:** No Redis password provided despite Redis requiring authentication
- **Fix:** Added `password=os.environ.get("REDIS_PASSWORD")`

## Bug 6
- **File:** `frontend/app.js`
- **Line:** 6
- **Problem:** Hardcoded `http://localhost:8000` as API URL — fails inside Docker
- **Fix:** Changed to `process.env.API_URL || "http://api:8000"`

## Bug 7
- **File:** `frontend/views/index.html`
- **Line:** 5
- **Problem:** Missing opening `<style>` tag causing CSS to render as visible text
- **Fix:** Added `<style>` tag before CSS rules

## Bug 8
- **File:** `frontend/views/index.html`
- **Line:** 39
- **Problem:** Mojibake character `â€"` instead of proper em dash due to encoding issue
- **Fix:** Replaced with clean `-` dash character and added `<meta charset="UTF-8">`

## Bug 9
- **File:** `api/.env`
- **Line:** 1-2
- **Problem:** Real credentials committed to repository — security risk
- **Fix:** Added `.env` to `.gitignore`, removed from git tracking, created `.env.example` with placeholder values

## Bug 10
- **File:** `api/requirements.txt`
- **Line:** 1-3
- **Problem:** Unpinned dependencies — non-reproducible builds
- **Fix:** Pinned all versions: `fastapi==0.104.1`, `uvicorn==0.24.0`, `redis==5.0.1`

## Bug 11
- **File:** `worker/requirements.txt`
- **Line:** 1
- **Problem:** Unpinned dependency — non-reproducible builds
- **Fix:** Pinned version: `redis==5.0.1`

## Bug 12
- **File:** `frontend/package.json`
- **Line:** 1-15
- **Problem:** No Node.js engine version specified and no ESLint configured for CI pipeline
- **Fix:** Added `engines` field requiring Node 18+, added ESLint as devDependency with lint script