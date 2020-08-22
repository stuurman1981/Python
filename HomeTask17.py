from logging import Logger, DEBUG, StreamHandler, Formatter

class OwnLogger(Logger):
    def __init__(self, name):
        super().__init__(name)
        self.setLevel(DEBUG)
        ch = StreamHandler()
        ch.setLevel(DEBUG)

        formatter = Formatter('%(name)s - %(levelname)s: %(message)s')
        ch.setFormatter(formatter)

        self.addHandler(ch)

