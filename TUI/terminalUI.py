from Helpers import ErrorHandler, PortHandler
from Helpers.Threads import Threads
from os import system, name
import sys


class TUIColor:
    LIGHTGRAY = '\033[90m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BLUE = "\033[34m"


class terminal:
    errors = ErrorHandler()

    @staticmethod
    def clear():
        return system('cls') if name == 'nt' else system('clear')

    @staticmethod
    def log(target, port, targets, found=False):
        current, last = targets.index(target) + 1, len(targets)
        if found:
            print('\r\x1b[K \033[36m*\033[0m \033[92m[{}/{}] Scanning {}:{}\033[0m'
                  .format(current, last, target, port), end='', flush=True)
        else:
            print('\r\x1b[K \033[36m*\033[0m [{}/{}] Scanning {}:{}'
              .format(current, last, target, port), end='', flush=True)

    @staticmethod
    def output(available_port: dict, runtime: float, hosts: list):
        handler = PortHandler()

        for target in available_port.keys():
            if available_port[target]:
                print(TUIColor.BOLD + TUIColor.OKGREEN + " ● " + TUIColor.ENDC + TUIColor.BOLD + "HOST: "
                      + TUIColor.ENDC + target)
                print("   ----------------------------------------------------")
                HEADERS = ["PORT", "STATE", "SERVICE"]
                WIDTH = 9

                for index, port in enumerate(available_port[target]):
                    if index == 0:
                        print(
                            "   " + TUIColor.BOLD + " ".join(
                                [HEADER.ljust(WIDTH) for HEADER in HEADERS]) + TUIColor.ENDC)
                    service = handler.descriptionFor(port)
                    print("   {} {} {}".format(str(port).ljust(WIDTH),
                                               "OPEN".ljust(WIDTH),
                                               service.ljust(WIDTH)))
            else:
                print(TUIColor.BOLD + TUIColor.LIGHTGRAY + " ● " + TUIColor.ENDC + TUIColor.BOLD + "HOST: " +
                      TUIColor.ENDC + target)
                print("   ----------------------------------------------------")

                print("   Open ports not detected")
            print(" ------------------------------------------------------\n")
        print(TUIColor.BOLD + " OUT:\n" + TUIColor.ENDC + " {} HOST SCANNED IN {} SECONDS".format(
            len(hosts), runtime) + "\n" + " LIVE THREADS: {0}\n".format(Threads.active_threads()))
        sys.exit()

    @staticmethod
    def banner():
        print("""
\033[36m
  _____  ________   _______  _      
 |  __ \|  ____\ \ / /  __ \| |        
 | |__) | |__   \ V /| |__) | |             
 |  ___/|  __|   > < |  ___/| |        
 | |    | |____ / . \| |    | |____    \033[1mAuthor:\033[0m  uxn0w\033[36m     
 |_|    |______/_/ \_\_|    |______|   \033[36m\033[1mVersion:\033[0m 1.0 

 \033[36m\033[1mGit:\033[0m github.com/uxn0w/Portexplorer\n
""")

    @staticmethod
    def help():
        print("""
\033[1mUsage:\033[0m ./portexplorer.py {-m MODE} {-r RANGE} [-t TARGETS]

\033[1mMODE -m:\033[0m
    0: Normal (80 threads)
    1: Faster (100 threads)
    2: Ultra (130 threads)
    Default: 80 threads

\033[1mPORT RANGE -r:\033[0m
    0: 1-9999 ports
    1: 1-49150 ports
    Default: 1-9999 ports

\033[1mEXAMPLES:\033[0m
  ./pexpl.py -t xxx.xxx.xxx.xxx xxx.xxx.xxx.xxx 
  ./pexpl.py -m 1 xxx.xxx.xxx.xxx
  ./pexpl.py -m 2 -r 1 list_targets        
        """)
        sys.exit()
