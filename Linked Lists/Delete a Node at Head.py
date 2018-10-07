# Remove an element from the head of a linkedlist: DSAIP


def remove_first(L):
    if L.head is None:
        return []
    L.head = L.head.next
    return L.head
