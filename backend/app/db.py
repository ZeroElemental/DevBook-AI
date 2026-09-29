"""SQLite access: connection setup, schema and migrations."""

import sqlite3
from collections.abc import Iterator

from app.config import settings

NOW = "strftime('%Y-%m-%dT%H:%M:%SZ','now')"

SCHEMA_V1 = f"""
CREATE TABLE IF NOT EXISTS books (
    id           TEXT PRIMARY KEY,
    title        TEXT NOT NULL,
    filename     TEXT NOT NULL,
    sha256       TEXT NOT NULL UNIQUE,
    size_bytes   INTEGER NOT NULL,
    page_count   INTEGER NOT NULL,
    chunk_count  INTEGER NOT NULL DEFAULT 0,
    status       TEXT NOT NULL DEFAULT 'queued'
                 CHECK (status IN ('queued','parsing','embedding','ready','failed')),
    progress     REAL NOT NULL DEFAULT 0 CHECK (progress BETWEEN 0 AND 1),
    error_code   TEXT,
    error        TEXT,
    warning      TEXT,
    created_at   TEXT NOT NULL DEFAULT ({NOW}),
    updated_at   TEXT NOT NULL DEFAULT ({NOW})
);

CREATE TABLE IF NOT EXISTS conversations (
    id          TEXT PRIMARY KEY,
    book_id     TEXT NOT NULL REFERENCES books(id) ON DELETE CASCADE,
    title       TEXT NOT NULL,
    created_at  TEXT NOT NULL DEFAULT ({NOW}),
    updated_at  TEXT NOT NULL DEFAULT ({NOW})
);
CREATE INDEX IF NOT EXISTS idx_conversations_book ON conversations(book_id, updated_at DESC);

CREATE TABLE IF NOT EXISTS messages (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    conversation_id  TEXT NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
    role             TEXT NOT NULL CHECK (role IN ('user','assistant')),
    content          TEXT NOT NULL,
    selection        TEXT,
    citations        TEXT,
    model            TEXT,
    stopped          INTEGER NOT NULL DEFAULT 0 CHECK (stopped IN (0,1)),
    created_at       TEXT NOT NULL DEFAULT ({NOW})
);
CREATE INDEX IF NOT EXISTS idx_messages_conv ON messages(conversation_id, id);
"""

# Index + 1 == schema version. Append new migrations; never edit old ones.
MIGRATIONS = [SCHEMA_V1]


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(settings.DB_PATH, timeout=5, isolation_level=None)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA busy_timeout = 5000")
    return conn


def migrate(conn: sqlite3.Connection) -> None:
    current = conn.execute("PRAGMA user_version").fetchone()[0]
    if current > len(MIGRATIONS):
        raise RuntimeError(
            f"Database schema version {current} is newer than this app supports ({len(MIGRATIONS)}). "
            "Update DevBook AI."
        )
    for version, sql in enumerate(MIGRATIONS[current:], start=current + 1):
        conn.executescript(f"BEGIN; {sql}; PRAGMA user_version = {version}; COMMIT;")


def get_conn() -> Iterator[sqlite3.Connection]:
    """FastAPI dependency: one connection per request."""
    conn = connect()
    try:
        yield conn
    finally:
        conn.close()
