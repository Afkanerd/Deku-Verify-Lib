"""Deku Verify Plugin"""

class Main():
    """Entry"""

    database_params = None

    @classmethod
    def __configure__(cls, database_params):
        """
        """
        cls.database_params = database_params

    def __init__(self, database_params: object = None) -> None:
        self.__configure__(database_params)

    def create(self):
        """Create Method"""

        from DekuVerify.models.verifications import Verification

        try:
            session = Verification()

            session_ = session.create()

            return {
                "code": session_.code,
                "sid": session_.sid,
                "expires": session_.expires
            }

        except Exception as error:
            raise error
