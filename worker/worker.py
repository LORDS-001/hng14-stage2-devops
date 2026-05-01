import redis
import time
import os

r = redis.Redis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=6379,
    password=os.environ.get("REDIS_PASSWORD")
)


def process_job(job_id):
    print(f"Processing job {job_id}")
    time.sleep(2)
    r.hset(f"job:{job_id}", "status", "completed")
    print(f"Done: {job_id}")


while True:
    job = r.brpop("job", timeout=5)
    if job:
        process_job(job[1].decode())
