# You’re given the pointer to the head node of a linked list, an integer to add to the list and the position at which the integer must be inserted. Create a new node with the given integer, insert this node at the desired position and return the head node.
# : https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem


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

# Alternative Solution:


def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)
    if position == 0:
        node.next = head
        return node
    current = head
    count = 0
    while current:
        if count + 1 == position:
            node.next = current.next
            current.next = node
        count += 1
        current = current.next
    return head
