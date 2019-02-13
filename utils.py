import sys

class WrongNumberOfArguments(Exception):
    def __init__(self, message):
        self.message = message


def validateUserInput():
    try:
        if(len(sys.argv) != 3):
            raise WrongNumberOfArguments(message = "Wrong number of arguments")

        _, origin, calling_at = sys.argv

        return (origin, calling_at)
    except WrongNumberOfArguments as e:
        sys.exit(e.message)
