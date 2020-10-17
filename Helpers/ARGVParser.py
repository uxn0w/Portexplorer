from sys import argv
from Helpers import Host
from TUI import terminal


def check_targets(function):
    def wrapper(self):

        try:
            option = argv.index("-t")
        except ValueError:
            return function(self, [])

        try:
            targets = argv[option + 1:]
            if not len(targets) >= 1:
                terminal.errors.TARGETSERROR()

            for _ in filter(lambda host: not Host.validate(host), targets):
                terminal.errors.TARGETSERROR()

            return function(self, targets)
        except Exception:
            terminal.errors.TARGETSERROR()

    return wrapper


def validate(argument: str, lim: int):
    def decorator(function):
        def wrapper(self):

            option, value = 0, 0
            try:
                option = argv.index(argument)
            except ValueError:
                return function(self, 0)

            try:
                value = int(argv[option + 1])
            except ValueError:
                terminal.errors.INVALIDARGERROR()
            except IndexError:
                terminal.errors.INVALIDARGERROR()

            return function(self, value) if value < lim else terminal.errors.VALUEERROR()

        return wrapper

    return decorator


class ARGVParser:

    @property
    @validate(argument="-r", lim=2)
    def port_range(self, value=0) -> int:
        return value

    @property
    @validate(argument="-m", lim=3)
    def mode(self, value=0) -> int:
        return value

    @property
    @check_targets
    def targets(self, targets=None) -> list:
        if targets:
            return targets
        else:
            host = input(" \033[36m>\033[0m Target (ex: google.com): ")
            if host:
                return [host]
            else: terminal.errors.BADHOST()
