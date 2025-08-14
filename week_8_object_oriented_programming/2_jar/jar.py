class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError("Capacity must be a positive integer!")
        self._capacity = capacity
        self._size = 0
    def __str__(self):
        return self.size * "🍪"
    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Too many cookies!")
        elif n + self.size > self.capacity:
            raise ValueError("Too many cookies!")
        self._size += n
    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Sorry, we don't have that much!")
        self._size -= n
    @property
    def capacity(self):
        return self._capacity
    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    print(Jar)

if __name__ == "__main__":
    main()
