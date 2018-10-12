class HashTable:
    class Pair:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, capacity=100):
        self.size = 0
        self.capacity = capacity
        self.map = [None] * self.capacity

    def load_factor(self):
        return self.size / self.capacity

    def hash_function(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)  # ord turns characters into ascii value
        return hash % self.capacity
        # or: return hash(key) % self.capacity

    def add(self, key, val):
        index = self.hash_function(key)
        entry = self.map[index]
        # This step is here because we're doing entry.next below, so we are skipping over the first element of the linked list.
        if entry is not None and entry.key == key:
            entry.value = value
            return True
        if entry is None:
            entry = self.Pair(key, val)
        else:
            while entry.next is not None:
                if entry.key == key:
                    # If the index is not empty, nor is the key, so we're just overriding.
                    entry.value = value
                    return True
                entry = entry.next
            entry.next = self.Pair(key, value)
            # If we traverse the whole linked list and doesn't return the same key, we are creating a new key value pair at that linked list element.
        self.size += 1
        if self.load_factor >= 0.5:
            self.resize()
        return True

    def delete(self, key):
        index = self.hash_function(key)
        if self.map[index] is None:
            raise KeyError(key)
        else:
            entry = self.map[index]
            if entry.key == key:  # If on first element, like on above.
                entry = entry.next
                self.size -= 1
                return True
            while entry is not None:
                next_entry = entry.next
                if next_entry is not None and next_entry.key == key:
                    entry.next = next_entry.next
                    self.size -= 1
                    return True
                entry = entry.next
            raise KeyError(key)  # If we don't find the key.

    def resize(self):
        old_map = self.map
        self.capacity = self.capacity * 2
        self.map = [None] * (self.capacity)
        self.size = 0
        for entry in old_map:
            while entry is not None:
                self.add(entry.key, entry.value)
                entry = entry.next
