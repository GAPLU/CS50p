class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n


    def withdraw(self, n):
        self.size -= n


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        self._capacity = capacity


    @property
    def size(self):
        return self._size


    @size.setter
    def size(self, size):
        if size < 0 or size > self.capacity:
            raise ValueError()
        self._size = size

'''
def main():
    jar = Jar(10)
    jar.deposit(9)
    jar.withdraw(5)
    print(jar.capacity)

if __name__ == "__main__":
    main()
'''