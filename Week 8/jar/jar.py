class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if ((self._size + n) > self._capacity):
            raise ValueError("Max Capacity reached")
        self._size += n

    def withdraw(self, n):
        if (self._size - n < 0):
            raise ValueError("Min Capacity reached")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity
    
    # @capacity.setter
    # def capacity(self, capacity):
    #     self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    # @size.setter
    # def size(self, size):
    #     if size < self.capacity:
    #         self._size = size

    
