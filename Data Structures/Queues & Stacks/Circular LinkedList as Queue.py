class CircularQueue:
    """Queue implementation using circular linked list for storage"""

    def __init__(self):
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def first(self):
        if self.isEmpty():
            return "List is empty"
        head = self.tail.next
        return head.value

    def dequeue(self):
        """Remove and return the first element of the queue"""
        if self.isEmpty():
            return "List is empty"
        oldHead = self.tail.next
        if self.size == 1:
            self.tail = None
        else:
            self.tail.next = oldHead.next
        self.size -= 1
        return oldHead.value

    def enqueue(self, item):
        """Add an element to the back of the queue"""
        newItem = self.Node(item)
        if self.isEmpty():
            newItem.next = newItem
        else:
            newItem.next = self.tail.next  # Which was the previous head
            self.tail.next = newest
        self.tail = newest
        self.size += 1

    def rotate(self):
        """Rotate front element to the back of the queue"""
        if self.size > 0:
            self.tail = self.tail.next
