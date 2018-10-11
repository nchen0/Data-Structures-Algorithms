# Insert the new node at the tail and just return the head of the updated linked list: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem


def InsertNodeAtTail(head, data):
    if head == None:
        return Node(data)
    else:
        if head.next == None:
            head.next = Node(data)
        else:
            Insert(head.next, data)
        return head

# If we had the reference of the tail:
# Assuming L is the linked list.


def InsertNodeAtTail(L, data):
    node = Node(data)
    node.next = None
    L.tail.next = node
    L.tail = node
    return L.tail
