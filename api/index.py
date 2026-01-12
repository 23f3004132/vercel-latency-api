from api.latency import app

# Re-export the FastAPI `app` from `api/latency.py` so Vercel's Python builder
# detects the FastAPI application and exposes the routes defined there.
