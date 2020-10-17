from Helpers import ARGVParser, Threads
from queue import Empty as QueueEmpty
from TUI import terminal
from queue import Queue

import threading
import socket
import time
import sys


class explorer:
    __startTime = time.time()
    __threads: Threads = None
    __lock = threading.Lock()
    __numberOfThreads = 0
    __queue = Queue()
    __looptime = 0.0
    __public = []
    __report = {}

    def __init__(self, builder: ARGVParser = None, targets: list = None):
        hosts = builder.targets if builder else targets
        self.hosts = [target.replace("http://", "").replace("https://", "") for target in hosts]
        self.__updateThreadsAt(builder.mode)
        self.__updateRangeAt(builder.port_range)

    def work(self):
        for target in self.hosts:

            self.__startTime = time.time()

            for port in self.port_range:
                self.__queue.put(port)

            self.__threads = Threads(
                [threading.Thread(target=self.__proc_q, args=(target,)) for _ in range(self.__numberOfThreads)])
            self.__threads.start()

            self.__queue.join()
            self.__threads.join()

            self.__report[target] = [port for port in self.__public if port]
            self.__public.clear()
            self.__looptime += self.__runtime()

        terminal.clear()
        self.__present()

    def __updateThreadsAt(self, t_mode):
        if t_mode == 0:
            self.__numberOfThreads = 80
        elif t_mode == 1:
            self.__numberOfThreads = 100
        else:
            self.__numberOfThreads = 130

    def __updateRangeAt(self, u_range):
        self.port_range = range(1, 9999) if u_range == 0 else range(1, 49150)

    def __proc_q(self, target):
        while True:
            try:
                port = self.__queue.get(block=False)
            except QueueEmpty:
                return
            else:
                try:
                    self.__connect(target, port)
                finally:
                    self.__queue.task_done()
            time.sleep(0.1)

    def __connect(self, target, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.4)

        try:
            sock.connect((target, port))
        except socket.error:
            terminal.log(target, port, self.hosts)
        else:
            with self.__lock:
                sock.close()
                self.__public.append(port)
                terminal.log(target, port, self.hosts, found=True)

    def __present(self):
        terminal.banner()
        terminal.output(available_port=self.__report,
                        runtime=self.__runtime(),
                        hosts=self.hosts)

    def __runtime(self) -> float:
        return round(time.time() - self.__startTime, 2)


if __name__ == "__main__":
    terminal.clear()
    terminal.banner()

    if len(sys.argv) == 1:
        host = input(" \033[36m>\033[0m Target (ex: google.com): ")
        if host:
            explorer(targets=[host]).work()
        else:
            terminal.errors.BADHOST()
    elif sys.argv[1] == "-help":
        terminal.help()
    else:
        explorer(builder=ARGVParser()).work()