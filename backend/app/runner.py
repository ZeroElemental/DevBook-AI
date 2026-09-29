"""Sandboxed Python/JavaScript execution in throwaway Docker containers."""

from app.models import RunResult

LANGS = {
    "python": ("python:3.12-alpine", ["python", "-"]),
    "javascript": ("node:22-alpine", ["node", "-"]),
}
OUTPUT_LIMIT = 64 * 1024
MAX_CODE_BYTES = 100 * 1024


def run_code(language: str, code: str) -> RunResult:
    """docker run --rm -i --network none ... with code on stdin; kills the container on timeout."""
    raise NotImplementedError
