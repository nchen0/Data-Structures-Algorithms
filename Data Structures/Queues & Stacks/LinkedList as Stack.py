# In designing a linked list with a stack, we need to decide whether to model the top of the stack at the head or at the tail of the list.
# Since we can efficiently insert and delete elements in constant time only at the head, we orient the top of the stack at the head of our list.


class Node:
        # To represent our individual nodes of the list, we develop a lightweight Node class. The class will never be directly exposed to the user of our stack class, so we will define it as a nonpublic, nested class of our Stack class.
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storate."""

    def __init__(self):
        """Create an empty stack"""
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self, item):
        """Add element item to the top of the stack, which is the head."""
        currentHead = self.head
        # If our Node class was declared inside the LinkedStack class, we would do: self.Node...
        self.head = Node(item)
        self.head.next = currentHead
        self.size += 1

    def top(self):
        """Return but not remove the element at the top of the stack"""
        if self.isEmpty():
            return "Stack is empty."
        return self.head.value

    def pop(self):
        """Remove and return the element from the top of stack(LIFO)"""
        if self.isEmpty():
            return ("Stack is empty")
        value = self.head.value  # Getting the head to return
        # Removing/replacing the head with the next element in the stack.
        self.head = self.head.next
        self.size -= 1
        return value
