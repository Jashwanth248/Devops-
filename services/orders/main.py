import os
from fastapi import FastAPI
from prometheus_client import Counter, make_asgi_app

app = FastAPI(title='PulseCart Orders', version='1.0.0')
DB_HOST = os.getenv('DB_HOST', 'postgres')
REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
ORDERS = Counter('orders_requests_total', 'Orders endpoint requests')
app.mount('/metrics', make_asgi_app())

@app.get('/healthz')
def healthz():
    return {'status': 'ok', 'service': 'orders'}

@app.get('/readyz')
def readyz():
    return {'ready': True, 'dependencies': {'postgres': DB_HOST, 'redis': REDIS_HOST}}

@app.get('/orders')
def list_orders():
    ORDERS.inc()
    return {'orders': [{'id': 'ord-1001', 'status': 'processing'}]}
