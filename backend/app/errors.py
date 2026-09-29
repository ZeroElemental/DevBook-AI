from fastapi import HTTPException


class ApiError(HTTPException):
    """Error with a stable machine-readable code: {"detail": {"code", "message", "hint"}}."""

    def __init__(self, status: int, code: str, message: str, hint: str | None = None, **extra):
        super().__init__(status, {"code": code, "message": message, "hint": hint, **extra})
