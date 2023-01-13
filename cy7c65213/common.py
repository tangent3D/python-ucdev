class GPIO(object):
    def pin(self, nr):
        return GPIOPin(self, nr)

class GPIOPin(object):
    def __init__(self, port, nr):
        self.port = port
        self.nr = nr

    def get(self):
        return self.port.get(self.nr)

    def set(self, val):
        return self.port.set(self.nr, val)
