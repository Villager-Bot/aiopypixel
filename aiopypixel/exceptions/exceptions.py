class Error(Exception):
    """class for other exceptions/errors"""

    def __init__(self, reason="Unknown reason!"):
        self.message = reason
        super().__init__(self.message)

    def __str__(self):
        return self.message


class RateLimitError(Exception):
    """Raised when a ratelimit is reached"""

    def __init__(self, source="unknown source"):
        self.message = f"A ratelimit was hit! ({source})"
        super().__init__(self.message)

    def __str__(self):
        return self.message


class InvalidPlayerError(Exception):
    """Raised when an invalid player name or uuid is provided"""

    def __init__(self, cause="unknown cause"):
        self.message = f"Invalid player name or uuid was provided! ({cause})"
        super().__init__(self.message)

    def __str__(self):
        return self.message
