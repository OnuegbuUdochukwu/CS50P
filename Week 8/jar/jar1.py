class Jar:
    def __init__(self, capacity=12):
        if int < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self.capacity = capacity

    def __str__(self):
        return f"{capacity * "🍪"}"

    def deposit(self, n):
        if (self.capacity + n > 12):
            raise ValueError("Max Capacity reached")

    def withdraw(self, n):
        if (self.capacity - n < 0):
            raise ValueError("Min Capacity reached")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        ...