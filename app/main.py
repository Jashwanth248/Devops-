import os
import random
import time

from fastapi import FastAPI, Response
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest

app = FastAPI(title="Cloud Native DevOps Platform", version="1.0.0")
REQ = Counter("http_requests_total", "HTTP requests", ["path", "status"])
LAT = Histogram("http_request_duration_seconds", "Request latency", ["path"])
START = time.time()


@app.get("/")
def root():
    REQ.labels("/", "200").inc()
    return {
        "service": "cloud-native-api",
        "env": os.getenv("APP_ENV", "local"),
        "version": os.getenv("APP_VERSION", "dev"),
    }


@app.get("/healthz")
def health():
    return {"status": "ok"}


@app.get("/readyz")
def ready():
    return {"ready": True, "uptime_s": round(time.time() - START, 2)}


@app.get("/work")
def work(delay_ms: int = 50, fail_rate: float = 0.0):
    with LAT.labels("/work").time():
        time.sleep(max(0, min(delay_ms, 3000)) / 1000)
        if random.random() < max(0, min(fail_rate, 1)):
            REQ.labels("/work", "500").inc()
            return Response("simulated failure", status_code=500)
        REQ.labels("/work", "200").inc()
        return {"status": "completed", "delay_ms": delay_ms}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
