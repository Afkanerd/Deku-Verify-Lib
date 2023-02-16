"""Verification Handler"""

import logging
from datetime import datetime, timedelta

from DekuVerify.schemas.deku_verify_sessions import DekuVerifySessions

logger = logging.getLogger(__name__)


class Verification:
    """Handler definition"""

    def __init__(self) -> None:
        self.deku_verify_sessions = DekuVerifySessions

    def __clean__(self) -> None:
        """Update expired session's status"""

        logger.debug("[*] initializing ...")

        age = datetime.now() - timedelta(minutes=10)

        session_ = self.deku_verify_sessions.update(status="expired",).where(
            (self.deku_verify_sessions.expires < age)
            & (self.deku_verify_sessions.status != "expired")
        )

        session_.execute()

        logger.info("[x] initialized")

    def create(self, identifier: str) -> object:
        """Create a verification instance

        Keyword arguments:
        identifier -- An identifier mapped to code

        return: object
        """

        self.__clean__()

        try:
            logger.debug("[*] Finding session for '%s' ...", identifier)

            session = self.deku_verify_sessions.get(
                self.deku_verify_sessions.identifier == identifier,
                self.deku_verify_sessions.status == "pending",
            )

        except self.deku_verify_sessions.DoesNotExist:
            try:
                logger.debug("[*] Creating verify session ...")

                session = self.deku_verify_sessions.create(
                    identifier=identifier, sent_attempts=1
                )

                logger.info("[X] Successfully created Verfiy Session")

                return session

            except Exception as error:
                logger.error("[!] Error creating verify session. See logs below")
                raise error

        else:
            logger.debug("[*] Updating session '%s' ...", str(session.sid))

            default_code_lifetime = datetime.now() + timedelta(minutes=10)

            session.sent_attempts += 1
            session.expires = default_code_lifetime
            session.save()

            return session
