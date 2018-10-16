# A linked list is a linear data structure in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers.
# We can identify the tail as the node having None as its next reference.
# There is not an absolute need to store a direct reference to the tail of the list, as it could otherwise be located by starting at the head and traversing the rest of the list. However, storing an explicit reference to the tail node is a common convenience to avoid such a traversal.

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


# With head/current, etc, it doesn't matter if we're returning back node (after doing node.next = head), or returning head, because everything references the same list. Because we assign current = head, anything that we change in the current linked list will affect the head linked list, as they're the same list. What we're returning back (the head), is just there so we can have a reference to the head of the linked list as we traverse through it with current.
