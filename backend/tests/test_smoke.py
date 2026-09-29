from app import db
from app.config import settings


def test_health(client):
    assert client.get("/health").status_code == 200


def test_schema_applied(client):
    conn = db.connect()
    try:
        assert conn.execute("PRAGMA user_version").fetchone()[0] == len(db.MIGRATIONS)
        tables = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    finally:
        conn.close()
    assert {"books", "conversations", "messages"} <= tables
    assert settings.BOOKS_DIR.is_dir() and settings.NOTES_DIR.is_dir()


def test_migrate_is_idempotent(client):
    conn = db.connect()
    try:
        db.migrate(conn)
        db.migrate(conn)
        assert conn.execute("PRAGMA user_version").fetchone()[0] == len(db.MIGRATIONS)
    finally:
        conn.close()
