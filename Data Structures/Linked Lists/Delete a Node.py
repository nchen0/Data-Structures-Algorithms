# You’re given the pointer to the head node of a linked list and the position of a node to delete. Delete the node at the given position and return the head node: https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem


def deleteNode(head, position):
    if position == 0:
        head = head.next
        return head
    count = 0
    current = head
    while current:
        if count + 1 == position:
            current.next = current.next.next
            return head
        current = current.next
        count += 1
    return head
