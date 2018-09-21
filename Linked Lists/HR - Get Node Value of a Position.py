# You’re given the pointer to the head node of a linked list and a specific position. Counting backwards from the tail node of the linked list, get the value of the node at the given position. A position of 0 corresponds to the tail, 1 corresponds to the node before the tail and so on.


def getNode(head, positionFromTail):
    current = head
    count = 0
    while current:
        count += 1
        current = current.next
    print('count is: {}'.format(count))
    target = count - positionFromTail
    print('target is: {}'.format(target))
    new_count = 1
    new_current = head
    while new_current:
        if new_count == target:
            return new_current.data
        else:
            new_current = new_current.next
            new_count += 1
