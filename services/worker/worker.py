import os
import time

QUEUE = os.getenv('QUEUE_NAME', 'order-events')

if __name__ == '__main__':
    print(f'worker started queue={QUEUE}', flush=True)
    while True:
        print('worker heartbeat', flush=True)
        time.sleep(30)
