class FatalException(Exception):
    pass


class UnsupportedSystem(FatalException):
    pass


class InvalidArgument(FatalException):
    pass
