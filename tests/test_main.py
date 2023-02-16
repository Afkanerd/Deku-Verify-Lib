"""Main Test Module"""

import os
import pytest

from DekuVerify import Verification, MySQL
from DekuVerify.exceptions import SessionNotFound, IncorrectCode, InvalidIdentifier

IDENTIFIER = "me"


@pytest.fixture
def plugin():
    """Initialize Deku Verify Plugin"""

    db_config = MySQL(
        database=os.environ["MYSQL_DATABASE"],
        user=os.environ["MYSQL_USER"],
        host=os.environ["MYSQL_HOST"],
        password=os.environ["MYSQL_PASSWORD"],
    )

    verify = Verification(database_params=db_config)

    return verify


def test_create(plugin):
    """Test Create Method"""

    result = plugin.create(IDENTIFIER)

    assert isinstance(result, dict)

    assert "code" in result
    assert "sid" in result
    assert "identifier" in result
    assert "expires" in result

    assert isinstance(result["code"], str)
    assert isinstance(result["sid"], str)
    assert isinstance(result["identifier"], str)
    assert isinstance(result["expires"], int)

    assert len(result["code"]) == 4


def test_check(plugin):
    """Test Check Method"""

    check_result = plugin.create(IDENTIFIER)
    sid = check_result["sid"]
    code = check_result["code"]
    identifier = check_result["identifier"]

    result = plugin.check(sid, identifier, code)

    assert isinstance(result, dict)

    assert "sid" in result
    assert "identifier" in result
    assert "status" in result

    assert isinstance(result["sid"], str)
    assert isinstance(result["identifier"], str)
    assert isinstance(result["status"], str)


def test_check_invalid_session(plugin):
    """Test Check Method with Invalid Session ID"""

    with pytest.raises(SessionNotFound):
        check_result = plugin.create(IDENTIFIER)
        sid = "invalid sid"
        code = check_result["code"]
        identifier = check_result["identifier"]

        plugin.check(sid, identifier, code)


def test_check_incorrect_code(plugin):
    """Test Check Method with Incorrect Code"""

    with pytest.raises(IncorrectCode):
        check_result = plugin.create(IDENTIFIER)
        sid = check_result["sid"]
        code = "Incorrect code"
        identifier = check_result["identifier"]

        plugin.check(sid, identifier, code)


def test_check_invalid_identifier(plugin):
    """Test Check Method with Invalid Identifier"""

    with pytest.raises(InvalidIdentifier):
        check_result = plugin.create(IDENTIFIER)
        sid = check_result["sid"]
        code = check_result["code"]
        identifier = "invalid identifier"

        plugin.check(sid, identifier, code)
