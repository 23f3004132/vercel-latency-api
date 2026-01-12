from fastapi import FastAPI
from api.latency import app as latency_app

# Root application Vercel will detect. Mount the existing latency app
app = FastAPI()
app.mount("/api/latency", latency_app)
