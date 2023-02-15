"""Deku Verify Database Credentials"""

class MySQL:
    """MySQL Client"""
    host=None
    user=None
    password=None
    database=None

    def __init__(self, host: str, user: str, password: str, database: str) -> None:
        self.host=host
        self.user=user
        self.password=password
        self.database=database
