class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.buffer = []

    def append(self, item):
        if self.capacity > len(self.buffer):
            self.buffer.append(item)
        elif self.capacity == len(self.buffer):
            self.buffer[self.current] = item
            self.current = (self.current + 1) % self.capacity

    def get(self):
        if self.buffer is not None:
            return self.buffer[:self.current]+self.buffer[self.current:]
