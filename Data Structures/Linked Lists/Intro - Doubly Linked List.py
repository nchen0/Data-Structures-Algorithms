# Doubly Linked Lists contain an extra pointer, the previous pointer together with the next pointer from the singly linked list.

"""
Advantages over singly linked lists:
1. A DLL can be traversed in both forward and backward direction.
2. The delete operation in DLL is more efficient if pointer to the node to be deleted is given.
3. We can quickly insert a new node before a given node. 
* In singly linked list, to delete a node, a pointer to the previous node is needed. To get this previous node, sometimes the list is traversed. In DLL, we already have a previous pointer pointing to the previous node.

Disadvantages over singly linked lists:
1. Every node of DLL requres extra space for a previous pointer. 
2. All operations require an extra pointer to be maintained. For example, in insertion, we need to modify previous pointers together with next pointers. 

Insertion: A node can be added in four ways
1) At the front of the DLL
2) After a given node.
3) At the end of the DLL
4) Before a given node.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this Node could already
  have a next node it is pointing to."""

    def insert_after(self, val):
        node = ListNode(val)
        if self.next:
            temp = self.next
            node.next = temp
            self.next = node
        else:
            self.next = node
    """Wrap the given value in a ListNode and insert it
  before this node. Note that this Node could already
  have a previous node it is pointing to."""

    def insert_before(self, val):
        node = ListNode(val)
        if self.prev:
            temp = self.prev
            node.prev = temp
            self.prev = node
        else:
            self.prev = node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, val):
        node = Node(val)
        if self.head:
            temp = self.head
            node.next = temp
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node

    def remove_from_head(self):
        if self.head:
            temp = self.head
            self.head.next.prev = None
            self.head = self.head.next
            return temp.val
        else:
            return None

    def add_to_tail(self, val):
        node = ListNode(val)
        if self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def remove_from_tail(self):
        if self.tail:
            temp = self.tail
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return temp.val
        else:
            return None

    def move_to_front(self, node):
        if node == self.tail:
            self.remove_from_tail()
        else:
            node.delete()
        self.add_to_head(node.val)

    def move_to_end(self, node):
        if node == self.head:
            self.remove_from_head()
        else:
            node.delete()
        self.add_to_tail(node.val)
