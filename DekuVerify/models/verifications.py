"""Verification Handler"""

import logging
from datetime import datetime, timedelta

from DekuVerify.schemas.deku_verify_sessions import DekuVerifySessions

from DekuVerify.exceptions import SessionNotFound, IncorrectCode, InvalidIdentifier

logger = logging.getLogger(__name__)


class Verification:
    """Handler definition"""

    def __init__(self) -> None:
        self.deku_verify_sessions = DekuVerifySessions

    def __clean__(self) -> None:
        """Update expired session's status"""

        logger.debug("[*] initializing ...")

        sessions = self.deku_verify_sessions.select()

        for session in sessions.iterator():
            age = session.expires.timestamp() - datetime.now().timestamp()

            if age <= 0:
                session_ = self.deku_verify_sessions.update(status="expired",).where(
                    self.deku_verify_sessions.sid == session.sid,
                    self.deku_verify_sessions.status == "pending",
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

    def check(self, sid: str, identifier: str, code: str) -> object:
        """Check verification status

        Keyword arguments:
        sid -- Verification session ID
        identifier -- An identifier mapped to code
        code -- verification code

        return: object
        """

        self.__clean__()

        try:
            logger.debug("[*] Finding session for '%s' ...", identifier)

            session = self.deku_verify_sessions.get(
                self.deku_verify_sessions.sid == sid,
                self.deku_verify_sessions.status == "pending",
            )

        except self.deku_verify_sessions.DoesNotExist:
            raise SessionNotFound

        else:
            session.verified_attempts += 1

            if session.identifier != identifier:
                session.save()

                raise InvalidIdentifier

            if session.code != code:
                session.save()

                raise IncorrectCode

            session.status = "approved"
            session.save()

            return session

    def cancel(self, sid: str) -> bool:
        """Check verification status

        Keyword arguments:
        sid -- Verification session ID

        return: bool
        """

        self.__clean__()

        try:
            logger.debug("[*] Finding session '%s' ...", sid)

            session = self.deku_verify_sessions.get(
                self.deku_verify_sessions.sid == sid,
                self.deku_verify_sessions.status == "pending",
            )

        except self.deku_verify_sessions.DoesNotExist:
            raise SessionNotFound

        else:
            session.status = "cancelled"
            session.save()

            return True
