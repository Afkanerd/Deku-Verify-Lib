"""Deku Verify Exceptions"""


class SessionNotFound(Exception):
    """SessionNotFound

    Exception raised when a verification session is not found
    """

    def __init__(self, message="Session Not Found"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Error: {self.message}"


class IncorrectCode(Exception):
    """IncorrectCode

    Exception raised when a given verification code is incorrect
    """

    def __init__(self, message="Incorrect Code"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Error: {self.message}"


class InvalidIdentifier(Exception):
    """InvalidIdentifier

    Exception raised when a given identifier is incorrect the mapped session
    """

    def __init__(self, message="Invalid Identifier"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Error: {self.message}"
