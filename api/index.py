from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.latency import app as latency_app

# Create a root application Vercel will detect, enable permissive CORS,
# and mount the latency app at /api/latency so the endpoint is available
# at https://<project>.vercel.app/api/latency with CORS headers present.
app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_methods=["*"],
	allow_headers=["*"],
)

app.mount("/api/latency", latency_app)
