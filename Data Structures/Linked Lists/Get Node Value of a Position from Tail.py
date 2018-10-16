# You’re given the pointer to the head node of a linked list and a specific position. Counting backwards from the tail node of the linked list, get the value of the node at the given position. A position of 0 corresponds to the tail, 1 corresponds to the node before the tail and so on.
# : https: // www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem


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

# Alternative Solution:


def getNode(head, positionFromTail):
    # get the length of the linked list (without counting the tail):
    length = 0
    current = head
    while current.next:
        current = current.next
        length += 1
    # get the position from the head:
    positionFromHead = length - positionFromTail
    if positionFromTail == 0:
        # Since we're at the tail already anyway
        return current.data
    else:
        # go through loop again:
        current = head
        while current:
            if positionFromHead > 0:
                positionFromHead -= 1
                current = current.next
            return current.data
