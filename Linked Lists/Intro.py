# A linked list is a linear data structure in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers.

# Example of a Linked List


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# Printing the elements of a linked list:


def printLinkedList(head):
    current = head
    while current:
        print(current.data)
        current = current.next
