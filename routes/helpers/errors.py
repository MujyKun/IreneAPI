class BaseError(Exception):
    """An abstract error."""

    def __init__(self, status_code=500, message=""):
        super(BaseError, self).__init__(message)
        self.status_code = status_code
        self.message = message

    def __str__(self) -> str:
        return str(self.dict())

    def dict(self) -> dict:
        """Return a dictionary of the error."""
        return {"code": self.status_code, "message": self.message}


class LackingPermissions(BaseError):
    """Raised when lacking permissions."""

    def __init__(self):
        super(LackingPermissions, self).__init__(
            status_code=403, message="You are lacking permissions."
        )


class InvalidLogin(BaseError):
    """Raised when an Invalid Login occurs."""

    def __init__(self):
        super(InvalidLogin, self).__init__(
            status_code=401, message="Could not authenticate the login."
        )


class BadRequest(BaseError):
    """Raised when there is a bad request (missing information or bad input)"""

    def __init__(self):
        super(BadRequest, self).__init__(
            status_code=400,
            message=f"Bad Request. Please follow the documentation for login at {'...'}",
        )
