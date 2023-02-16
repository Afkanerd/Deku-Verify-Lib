"""Deku Verify Plugin"""


class Main:
    """Entry"""

    database_params = None

    @classmethod
    def __configure__(cls, database_params):
        """ """
        cls.database_params = database_params

    def __init__(self, database_params: object = None) -> None:
        self.__configure__(database_params)

    def create(self, identifier: str):
        """Create Method"""

        from DekuVerify.models.verifications import Verification

        try:
            session = Verification()

            session_ = session.create(identifier)

            return {
                "code": str(session_.code),
                "sid": str(session_.sid),
                "identifier": session_.identifier,
                "expires": int(round(session_.expires.timestamp())) * 1000,
            }

        except Exception as error:
            raise error

    def check(self, sid: str, identifier: str, code: str):
        """Check Method"""

        from DekuVerify.models.verifications import Verification

        try:
            session = Verification()

            session_ = session.check(sid, identifier, code)

            return {
                "sid": str(session_.sid),
                "identifier": session_.identifier,
                "status": session_.status,
            }

        except Exception as error:
            raise error

    def cancel(self, sid: str):
        """Cancel Method"""

        from DekuVerify.models.verifications import Verification

        try:
            session = Verification()

            session_ = session.cancel(sid)

            return session_

        except Exception as error:
            raise error
