# You’re given the pointer to the head node of a linked list. Change the next pointers of the nodes so that their order is reversed. The head pointer given may be null meaning that the initial list is empty.


def reverse(head):
    current = head
    prev = None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev
