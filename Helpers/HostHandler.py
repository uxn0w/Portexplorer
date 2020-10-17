import re


class Host:
    @staticmethod
    def validate(host: str):
        # Try to check the target using a regular expression for the ip address and domain name.
        # Return a target, or None if no match was found.
        ip = re.findall('^(?=\d+\.\d+\.\d+\.\d+$)(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.?){4}$', host)
        domain = re.findall('^((?!-)[A-Za-z0-9-]{1,63}(?<!-)\\.)+[A-Za-z]{2,6}$', host)
        return host if ip or domain else None

