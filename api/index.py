from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.latency import router as latency_router

# Root application Vercel will detect. Enable permissive CORS and include
# the latency router so its operations appear in the root OpenAPI spec.
app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_methods=["*"],
	allow_headers=["*"],
)

app.include_router(latency_router, prefix="/api/latency")


@app.get("/", include_in_schema=False)
async def health():
    return {"status": "ok"}

