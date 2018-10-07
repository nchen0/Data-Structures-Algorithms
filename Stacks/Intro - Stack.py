# Stacks are LIFO, array-like data structures. Although a list could be used in place of a formal stack class, lists include behaviros that would break the abstraction that the stack data type represents.
# Stacks are implemented using lists.
# As a consequence of the LIFO protocol, a stack can be used as a general tool to reverse a data sequence.


class Stack:
    def __init__(self):
        """Creates an empty stack"""
        self.data = []

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self.data)

    def isEmpty(self):
        """Return True if the stack is empty"""
        return len(self.data) == 0

    def push(self, item):
        """Add element item to the top of the stack."""
        self.data.append(item)

    def top(self):
        """Return (but not remove) the element at the top of the stack"""
        return self.data[-1]

    def pop(self):
        """Remove and return the element from the top of the stack (LIFO)"""
        return self.data.pop()
