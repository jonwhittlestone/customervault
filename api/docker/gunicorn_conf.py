
import multiprocessing
import os

import gunicorn

host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "7998")
gunicorn.SERVER = "undisclosed"
gunicorn.SERVER_SOFTWARE = "undisclosed"

bind = [f"{host}:{port}"]
reload = True
workers = 4  # multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
