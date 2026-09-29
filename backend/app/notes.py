"""Per-book Markdown notes with atomic writes and mtime-based conflict detection."""

from app.models import NotesDoc


def read(book_id: str) -> NotesDoc:
    raise NotImplementedError


def write(book_id: str, content: str, base_version: str | None, force: bool) -> NotesDoc:
    raise NotImplementedError


def append(book_id: str, text: str, page: int) -> NotesDoc:
    raise NotImplementedError


def format_quote(text: str, page: int) -> str:
    raise NotImplementedError
