"""Retrieval and streamed, citation-grounded answers (NDJSON)."""

from collections.abc import AsyncIterator

from app.models import ChatRequest


async def retrieve(book_id: str, query: str) -> list:
    """The only caller of collection.query; always filters by book_id."""
    raise NotImplementedError


def citations_from(hits: list) -> list[dict]:
    raise NotImplementedError


async def stream_answer(book: dict, conversation_id: str, history: list[dict],
                        req: ChatRequest) -> AsyncIterator[bytes]:
    """Yields meta -> token* -> citations -> done (or error). Saves the answer in `finally`."""
    raise NotImplementedError
    yield b""  # pragma: no cover  (marks this as an async generator)
