import sys


class ErrorHandler:

    @staticmethod
    def TARGETSERROR():
        print("\033[31mError:\033[0m Invalid targets\n")
        sys.exit()

    @staticmethod
    def VALUEERROR():
        print("\033[31mError:\033[0m Incorrect option value\n")
        sys.exit()

    @staticmethod
    def INVALIDARGERROR():
        print("\033[31mError:\033[0m Invalid arguments")
        sys.exit()

    @staticmethod
    def BADHOST():
        print("\033[31mError:\033[0m Enter the host name (ex: google.com)\n")
