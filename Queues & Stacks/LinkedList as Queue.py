# Because we need to perform operations on both ends of the queue, we will explicitly maintain both a head and a tail reference.
# We implement a queue with the head as the front and tail as the back because we must be able to enqueue elements at the back, and dequeue them from the front, in FIFO fashion.
# We are unable to efficiently remove elements from the tail of a singly linked list, so this order is perfect for us.


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size

    def first(self):
        return self.head.value

    def dequeue(self):
        """Remove and return the first element of the queue"""
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        if self.ieEmpty():
            self.tail = None
        return value

    def enqueue(self, item):
        """Add an element to the back of the queue"""
        node = self.Node(item)
        if self.isEmpty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1
