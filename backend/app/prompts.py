"""Prompt text and token budgeting for grounded answers."""

import math

from app.models import Selection


def estimate_tokens(text: str) -> int:
    """Pessimistic estimate; no local tokenizer for the chat model."""
    return math.ceil(len(text) / 3.5)


def format_context(hits: list) -> str:
    raise NotImplementedError


def format_user(message: str, selection: Selection | None) -> str:
    raise NotImplementedError


def build_messages(title: str, hits: list, history: list[dict], message: str,
                   selection: Selection | None, weak: bool) -> list[dict]:
    raise NotImplementedError
