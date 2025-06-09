import os

bind = f"0.0.0.0:{os.environ.get('PORT', '8001')}"
workers = 1
worker_class = 'geventwebsocket.gunicorn.workers.GeventWebSocketWorker'
timeout = 300
