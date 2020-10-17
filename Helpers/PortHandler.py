import json

"""
Service Name and Transport Protocol Port Number Registry

Last Updated
    2020-09-22
--------------------------------------------------------
Expert(s)
    TCP/UDP: Joe Touch; Eliot Lear, Allison Mankin, Markku Kojo, Kumiko Ono, Martin Stiemerling,
    Lars Eggert, Alexey Melnikov, Wes Eddy, Alexander Zimmermann, Brian Trammell, and Jana Iyengar
    SCTP: Allison Mankin and Michael Tuexen
    DCCP: Eddie Kohler and Yoshifumi Nishida

Reference [RFC6335]
--------------------------------------------------------
Source:
https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml
"""


class PortHandler:

    def __init__(self):
        self.__load_json()

    def descriptionFor(self, port: int) -> str:
        try:
            return self.__kvp[str(port)]
        except KeyError:
            return "Undefined"

    def __load_json(self):
        with open("Helpers/Collection/service-names.json", "r") as data:
            self.__kvp = json.load(data)
