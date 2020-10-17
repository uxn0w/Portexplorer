import threading


class Threads:

    def __init__(self, threads):
        self.__threads = threads

    def join(self):
        for thread in self.__threads: thread.join()

    def start(self):
        for thread in self.__threads: thread.start()

    @staticmethod
    def active_threads(): return threading.active_count()