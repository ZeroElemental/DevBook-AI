"""The single ChromaDB client and `chunks` collection.

Created lazily so importing the app doesn't touch the vector store.
"""

from functools import cache


@cache
def collection():
    """PersistentClient at settings.CHROMA_DIR, collection 'chunks', cosine space, no embedding function."""
    raise NotImplementedError
