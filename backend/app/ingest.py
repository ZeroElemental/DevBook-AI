"""Upload validation and the single-threaded ingestion worker (Docling -> chunks -> embeddings -> Chroma)."""

from collections.abc import Callable

from fastapi import UploadFile

Embedder = Callable[[list[str]], list[list[float]]]


def save_upload(file: UploadFile) -> dict:
    """Stream to books/{id}.pdf.part, validate, dedupe by SHA-256, insert the row and enqueue."""
    raise NotImplementedError


def recover_and_start() -> None:
    """Mark interrupted ingests as failed, re-enqueue queued books, start the worker thread."""
    raise NotImplementedError


def enqueue(book_id: str) -> None:
    raise NotImplementedError


def run_ingest(book_id: str, embed: Embedder | None = None) -> None:
    """parsing -> embedding -> ready (or failed with an error code)."""
    raise NotImplementedError
