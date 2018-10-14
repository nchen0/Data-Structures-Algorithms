# You’re given the pointer to the head node of a linked list and the position of a node to delete. Delete the node at the given position and return the head node.


def deleteNode(head, position):
    if position > 0:
        current = head
        count = 0
        while current:
            if count == position - 1:
                current.next = current.next.next
                count += 1
            else:
                current = current.next
                count += 1
        return head
    else:
        head = head.next
        return head
