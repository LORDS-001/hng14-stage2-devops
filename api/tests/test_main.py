import pytest
from unittest.mock import MagicMock, patch


# Mock redis before importing app
mock_redis_instance = MagicMock()


with patch('redis.Redis', return_value=mock_redis_instance):
    from fastapi.testclient import TestClient
    from main import app


client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_mocks():
    mock_redis_instance.reset_mock()


# Test 1 - Create job returns job_id
def test_create_job_returns_job_id():
    mock_redis_instance.lpush.return_value = 1
    mock_redis_instance.hset.return_value = 1

    response = client.post("/jobs")

    assert response.status_code == 200
    data = response.json()
    assert "job_id" in data
    assert len(data["job_id"]) > 0


# Test 2 - Create job pushes to redis queue
def test_create_job_pushes_to_queue():
    mock_redis_instance.lpush.return_value = 1
    mock_redis_instance.hset.return_value = 1

    response = client.post("/jobs")

    assert response.status_code == 200
    mock_redis_instance.lpush.assert_called_once()
    mock_redis_instance.hset.assert_called_once()


# Test 3 - Get job status returns queued
def test_get_job_status_returns_status():
    mock_redis_instance.hget.return_value = b"queued"

    response = client.get("/jobs/test-job-123")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "queued"
    assert data["job_id"] == "test-job-123"


# Test 4 - Get job not found
def test_get_job_not_found():
    mock_redis_instance.hget.return_value = None

    response = client.get("/jobs/nonexistent-job")

    assert response.status_code == 200
    data = response.json()
    assert "error" in data


# Test 5 - Create job sets initial status to queued
def test_create_job_sets_queued_status():
    mock_redis_instance.lpush.return_value = 1
    mock_redis_instance.hset.return_value = 1

    response = client.post("/jobs")
    job_id = response.json()["job_id"]

    mock_redis_instance.hset.assert_called_with(
        f"job:{job_id}", "status", "queued"
    )
