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


class DoublyLinkedList:
