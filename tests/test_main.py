"""Main Test Module"""

import os
import pytest

from DekuVerify import Verification, MySQL

@pytest.fixture
def plugin():
    """Initialize Deku Verify Plugin"""

    db_config = MySQL(
        database=os.environ["MYSQL_DATABASE"],
        user=os.environ["MYSQL_USER"],
        host=os.environ["MYSQL_HOST"],
        password=os.environ["MYSQL_PASSWORD"]
    )

    verify = Verification(database_params=db_config)

    return verify

def test_create(plugin):
    """Test Create Method"""

    result = plugin.create()

    assert isinstance(result, dict)
    assert "code" in result
    assert "sid" in result
    assert "expires" in result
    assert isinstance(result["code"], int)
    assert isinstance(result["sid"], str)
    assert isinstance(result["expires"], int)
