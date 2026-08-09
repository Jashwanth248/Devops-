import os
import time
import requests
from fastapi import FastAPI, HTTPException
from prometheus_client import Counter, Histogram, make_asgi_app

app = FastAPI(title='PulseCart Gateway', version='1.0.0')
ORDERS_URL = os.getenv('ORDERS_URL', 'http://orders:8081')
REQUESTS = Counter('gateway_requests_total', 'Gateway requests', ['route', 'status'])
LATENCY = Histogram('gateway_request_duration_seconds', 'Gateway latency', ['route'])
app.mount('/metrics', make_asgi_app())

@app.get('/healthz')
def healthz():
    return {'status': 'ok', 'service': 'gateway'}

@app.get('/readyz')
def readyz():
    return {'ready': True}

@app.get('/api/orders')
def list_orders():
    start = time.perf_counter()
    try:
        r = requests.get(f'{ORDERS_URL}/orders', timeout=2)
        REQUESTS.labels('/api/orders', str(r.status_code)).inc()
        r.raise_for_status()
        return r.json()
    except requests.RequestException as exc:
        REQUESTS.labels('/api/orders', '503').inc()
        raise HTTPException(status_code=503, detail='orders service unavailable') from exc
    finally:
        LATENCY.labels('/api/orders').observe(time.perf_counter() - start)
