"""
- The hard part about linear probing is that using deleting an item can't be just set to None. If it's just set to None and we're searching for it, we might terminate the get too early, so a solution would be to set a sentinel marker, an object marker where that spot is. 
"""


class HashTable:

    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.map = [None] * self.capacity
        # This is used as a sentinel value to mark the location of previous deletions.
        self.is_deleted = object()

    def hash_function(self, key):
        return hash(key) % self.capacity

    def load_factor(self):
        return self.size / self.capacity

    def find_index(self, key):
        """Linear Probing: If the index is occupied, we insert into the next index"""
        index = self.hash_function(key)
        # Scenario 1, the index we're looking for is empty
        if self.map[index] is None:
            raise KeyError
        # Scenario 2, the index doesn't match the key,
        while self.map[index][0] != key:
            # Scenario 2b: if the index is a previously deleted object, raise key error, because the key has already been deleted.
            if self.map[index] == self.is_deleted:
                return KeyError
            index = (index + 1) % self.capacity
        return index

    def add(self, key, value):
        index = self.hash_function(key)
        pair = [key, value]
        self.size += 1
        # Scenario 1: If the index is None or is a deleted node, we add the key, value pair.
        if self.map[index] is None or self.map[index] == self.is_deleted:
            self.map[index] = pair
            return
        # Scenario 2: if the key is the same, we overwrite the value.
        if self.map[index][0] == key:
            self.map[index] = pair
            return
        # Scenario 3: If the index is not empty, and is not a deleted node, we traverse the array until we get to either an empty index or a deleted element, then we add the key, value pair.
        while self.map[index] is not None and self.map[index] is not self.is_deleted:
            index = (index + 1) % self.capacity
        self.map[index] = pair

        # Need to resize if the load factor gets too large.
        if float(self.load_factor()) >= 0.75:
            self.resize()

    def get(self, key):
        index = self.find_index(key)
        return self.map[index]

    def delete(self, key):
        index = self.find_index(key)
        if self.map[index] is not None:
            if self.map[index][0] == key:
                self.map[index] = self.is_deleted
                self.size -= 1

    def resize(self):
        self.capacity *= 2
        self.size = 0
        oldMap = self.map
        self.map = [None] * self.capacity
        for index, entry in enumerate(oldMap):
            if entry is not None:
                self.map[index] = entry


new_hash = HashTable()
new_hash.add(2, 3)
new_hash.add(3, 4)
new_hash.add(4, 4)
new_hash.add(5, 4)
new_hash.add(6, 4)
new_hash.delete(2)
new_hash.add(32, 5)
new_hash.add(42, 5)
new_hash.add(52, 5)

new_hash.add(62, 5)

new_hash.add(72, 5)

print(new_hash.get(5))
print(new_hash.get(32))
print(new_hash.get(72))
print(new_hash.get(62))


print(new_hash.map)
