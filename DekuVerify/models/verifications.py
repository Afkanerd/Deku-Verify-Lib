"""Verification Handler"""

import logging
from datetime import datetime

from DekuVerify.schemas.deku_verify_sessions import DekuVerifySessions

logger = logging.getLogger(__name__)

class Verification:
    """Handler definition"""

    def __init__(self) -> None:
        self.deku_verify_sessions = DekuVerifySessions

    def __clean__(self) -> None:
        """Update expired session's status"""
        sessions = self.deku_verify_sessions.select()

        logger.debug("[*] initialized ...")

        for session in sessions.iterator():
            age = session.expires.timestamp() - datetime.now().timestamp()

            if age <= 0:
                session_ = self.deku_verify_sessions.update(
                    status="expired",
                ).where(
                    self.deku_verify_sessions.sid == session.sid,
                )

                session_.execute()

        logger.info("[x] initialized")

    def create(self) -> object:
        """Create a verification instance
        
        Keyword arguments:

        return: object
        """

        self.__clean__()

        logger.debug("[*] Creating verify session ...")

        verify_session = self.deku_verify_sessions.create()

        logger.info("[X] Successfully created Verfiy Session")

        return verify_session
