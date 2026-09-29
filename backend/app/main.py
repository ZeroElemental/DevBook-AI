import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import db
from app.config import settings

logging.basicConfig(level=settings.LOG_LEVEL, format="%(asctime)s %(levelname)s %(name)s %(message)s")
log = logging.getLogger("devbook")


def _cleanup_temp_files() -> None:
    for pattern, folder in (("*.part", settings.BOOKS_DIR), ("*.md.tmp", settings.NOTES_DIR)):
        for path in folder.glob(pattern):
            path.unlink(missing_ok=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    for folder in (settings.BOOKS_DIR, settings.NOTES_DIR, settings.CHROMA_DIR):
        folder.mkdir(parents=True, exist_ok=True)
    conn = db.connect()
    try:
        db.migrate(conn)
    finally:
        conn.close()
    _cleanup_temp_files()
    log.info("data dir %s", settings.DATA_DIR)
    yield


app = FastAPI(title="DevBook AI", version="0.1.0", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.CORS_ORIGIN],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict:
    # Placeholder until the Ollama/Docker probes land (see app/health.py).
    return {"status": "ok"}
