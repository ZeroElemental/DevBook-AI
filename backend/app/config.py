"""Settings loaded once from DEVBOOK_* environment variables."""

import os
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def _int(name: str, default: int, lo: int, hi: int) -> int:
    raw = os.environ.get(name, str(default))
    try:
        value = int(raw)
    except ValueError:
        raise ValueError(f"{name} must be an integer, got {raw!r}") from None
    if not lo <= value <= hi:
        raise ValueError(f"{name} must be between {lo} and {hi}, got {value}")
    return value


def _float(name: str, default: float, lo: float, hi: float) -> float:
    raw = os.environ.get(name, str(default))
    try:
        value = float(raw)
    except ValueError:
        raise ValueError(f"{name} must be a number, got {raw!r}") from None
    if not lo <= value <= hi:
        raise ValueError(f"{name} must be between {lo} and {hi}, got {value}")
    return value


def _bool(name: str, default: bool) -> bool:
    raw = os.environ.get(name, "1" if default else "0")
    if raw not in ("0", "1"):
        raise ValueError(f"{name} must be 0 or 1, got {raw!r}")
    return raw == "1"


def _str(name: str, default: str) -> str:
    value = os.environ.get(name, default).strip()
    if not value:
        raise ValueError(f"{name} must not be empty")
    return value


@dataclass(frozen=True)
class Settings:
    DATA_DIR: Path
    CHAT_MODEL: str
    EMBED_MODEL: str
    OLLAMA_URL: str
    TOP_K: int
    NUM_CTX: int
    MAX_DISTANCE: float
    KEEP_ALIVE: str
    MAX_UPLOAD_MB: int
    MAX_PAGES: int
    RUN_TIMEOUT: int
    OCR: bool
    CORS_ORIGIN: str
    LOG_LEVEL: str

    @property
    def DB_PATH(self) -> Path:
        return self.DATA_DIR / "app.db"

    @property
    def CHROMA_DIR(self) -> Path:
        return self.DATA_DIR / "chroma"

    @property
    def BOOKS_DIR(self) -> Path:
        return self.DATA_DIR / "books"

    @property
    def NOTES_DIR(self) -> Path:
        return self.DATA_DIR / "notes"


def load() -> Settings:
    ollama_url = _str("DEVBOOK_OLLAMA_URL", "http://127.0.0.1:11434")
    if not ollama_url.startswith("http"):
        raise ValueError(f"DEVBOOK_OLLAMA_URL must start with http, got {ollama_url!r}")
    return Settings(
        DATA_DIR=Path(os.environ.get("DEVBOOK_DATA_DIR", REPO_ROOT / "data")).resolve(),
        CHAT_MODEL=_str("DEVBOOK_CHAT_MODEL", "qwen2.5-coder:7b"),
        EMBED_MODEL=_str("DEVBOOK_EMBED_MODEL", "nomic-embed-text"),
        OLLAMA_URL=ollama_url,
        TOP_K=_int("DEVBOOK_TOP_K", 6, 1, 20),
        NUM_CTX=_int("DEVBOOK_NUM_CTX", 8192, 2048, 131072),
        MAX_DISTANCE=_float("DEVBOOK_MAX_DISTANCE", 0.6, 0.0, 2.0),
        KEEP_ALIVE=_str("DEVBOOK_KEEP_ALIVE", "10m"),
        MAX_UPLOAD_MB=_int("DEVBOOK_MAX_UPLOAD_MB", 200, 1, 2000),
        MAX_PAGES=_int("DEVBOOK_MAX_PAGES", 2000, 1, 100_000),
        RUN_TIMEOUT=_int("DEVBOOK_RUN_TIMEOUT", 10, 1, 60),
        OCR=_bool("DEVBOOK_OCR", False),
        CORS_ORIGIN=_str("DEVBOOK_CORS_ORIGIN", "http://localhost:3000"),
        LOG_LEVEL=_str("DEVBOOK_LOG_LEVEL", "INFO").upper(),
    )


settings = load()
