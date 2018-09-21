# Insert a node at the head of a linked list.
# Insert the new node at the head and return the head of the updated linked list.


def insertNodeAtHead(llist, data):
    node = SinglyLinkedListNode(data)
    node.next = llist
    return node
