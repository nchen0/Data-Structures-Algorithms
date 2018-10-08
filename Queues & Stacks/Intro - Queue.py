# Queues follow a FIFO (First in first out) approach.
# It's tempting to use a similar approach as stack for implementing the queue, with an array, but it becomes tragically inefficient. When pop is called on a list with a non-default index, a loop is executed to shift all elements beyond the specified index to the left, so as to fill the hole in the sequence caused by the pop. Therefore, a call to pop(0) always causes the worst-case behavior of O(n) time.


# Implentation with a normal array (see above, can be inefficient)
class Queue:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.data == []

    def enqueue(self, item):
        self.data.insert(0, item)

    def dequeue(self):
        return self.data.pop(0)

    def size(self):
        return len(self.data)


# An implementation of a more 'efficient' way to make a queue is in DSAiP, but Python has an implementation of a deque class for us already (deque class = a double ended queue, or FIFO/LILO)
from collections import deque
D = dequeue()
D.append('j')
D.appendleft('f')
