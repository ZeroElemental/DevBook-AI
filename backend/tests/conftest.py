import os
import tempfile

import pytest

# Must be set before `app` is imported anywhere.
os.environ["DEVBOOK_DATA_DIR"] = tempfile.mkdtemp(prefix="devbook-test-")


@pytest.fixture
def client():
    from fastapi.testclient import TestClient

    from app.main import app

    with TestClient(app) as c:
        yield c
