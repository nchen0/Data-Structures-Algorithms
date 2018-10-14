class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = [None] * self.capacity

    def __str__(self):
        return str(self.map)

    def hash_function(self, key):
        return hash(key) % self.capacity

    def find_index(self, key):
        index = self.hash_function(key)
        while self.map[index] is not None and self.map[index][0] != key:
            index = (index + 1) % self.capacity
        return index

    def add(self, key, value):
        index = self.find_index(key)
        pair = [key, value]
        if self.map[index] != key:
            self.map[index] = pair
            self.count += 1

    def get(self, key):
        index = self.find_index(key)
        if self.map[index] is not None:
            return self.map[index]
        else:
            return KeyError(key)

    def delete(self, key):
