# Insert the new node at the tail and just return the head of the updated linked list.


def Insert(head, data):
    if head == None:
        return Node(data)
    else:
        if head.next == None:
            head.next = Node(data)
        else:
            Insert(head.next, data)
        return head
