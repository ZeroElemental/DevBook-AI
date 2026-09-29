"""API request/response models. Mirrored in frontend/lib/types.ts."""

from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field

BookStatus = Literal["queued", "parsing", "embedding", "ready", "failed"]


class Book(BaseModel):
    id: UUID
    title: str
    filename: str
    size_bytes: int
    page_count: int
    chunk_count: int
    status: BookStatus
    progress: float
    error_code: str | None
    error: str | None
    warning: str | None
    created_at: str
    updated_at: str


class Selection(BaseModel):
    text: str = Field(min_length=1, max_length=4000)
    page: int = Field(ge=1)


class ChatRequest(BaseModel):
    book_id: UUID
    conversation_id: UUID | None = None
    message: str = Field(min_length=1, max_length=4000)
    selection: Selection | None = None


class Citation(BaseModel):
    page: int
    page_end: int
    heading: str


class ConversationSummary(BaseModel):
    id: UUID
    title: str
    updated_at: str


class Message(BaseModel):
    id: int
    role: Literal["user", "assistant"]
    content: str
    selection: Selection | None
    citations: list[Citation] | None
    model: str | None
    stopped: bool
    created_at: str


class NotesDoc(BaseModel):
    content: str
    version: str | None
    updated_at: str | None


class NotesPut(BaseModel):
    content: str = Field(max_length=2_000_000)
    base_version: str | None
    force: bool = False


class NotesAppend(BaseModel):
    text: str = Field(min_length=1, max_length=4000)
    page: int = Field(ge=1)


class RunRequest(BaseModel):
    language: Literal["python", "javascript"]
    code: str = Field(min_length=1)


class RunResult(BaseModel):
    stdout: str
    stderr: str
    exit_code: int | None
    timed_out: bool
    duration_ms: int
