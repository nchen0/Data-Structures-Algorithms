# You’re given the pointer to the head node of a linked list, an integer to add to the list and the position at which the integer must be inserted. Create a new node with the given integer, insert this node at the desired position and return the head node.


def insertNodeAtPosition(head, data, position):
    current = head
    count = 0
    node = SinglyLinkedListNode(data)
    while current:
        if count == position - 1:
            temp = current.next
            current.next = node
            current.next.next = temp
            count += 1
        else:
            current = current.next
            count += 1
    return head

    """
    current = head
    for _ in range(position - 1):
        current = current.next
    temp = current.next
    current.next = SinglyLinkedListNode(data)
    current.next.next = temp
    return current
    """
