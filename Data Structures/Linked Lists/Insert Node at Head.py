# Insert a node at the head of a linked list: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
# Insert the new node at the head and return the head of the updated linked list.

# llist is the head of a linked list.


def insertNodeAtHead(llist, data):
    node = SinglyLinkedListNode(data)
    node.next = llist
    return node


# When using a singly linked list, we can easily insert an element at the head of the list inexpensively.
# Another variation of the above, with the first parameter being the linkedlist itself.
def insertNodeAtHead(L, data):
    node = Node(data)
    node.next = L.head
    L.head = node
    return L.head
