"""Setup checks for Ollama, the configured models and Docker."""


async def check() -> dict:
    """Probe Ollama (/api/version, /api/tags) and Docker concurrently, 3 s each."""
    raise NotImplementedError


def normalize_model(name: str) -> str:
    """'nomic-embed-text' -> 'nomic-embed-text:latest' so tags compare exactly."""
    return name if ":" in name else f"{name}:latest"
