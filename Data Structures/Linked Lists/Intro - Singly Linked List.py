# A linked list is a linear data structure in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers.
# We can identify the tail as the node having None as its next reference.
# There is not an absolute need to store a direct reference to the tail of the list, as it could otherwise be located by starting at the head and traversing the rest of the list. However, storing an explicit reference to the tail node is a common convenience to avoid such a traversal.
"""
- Advantages of Arrays vs Linked Lists:
    - Arrays provide O(1) access to an element based on an integer index, whereas linkedlists only have it for head and maybe tail. The ability to access elements at O(1) is a hallmark of arrays. In contrast, linked lists does it at O(n).
    - Arrays typically use proportionally less memory than linked lists. This may sound counterintuitive, especially given that the length of a dynamic array may be longer than the number of elements it stores. 
        - What differs is the auxiliary amount of memory that are used by the two structures. For an array-based container of n elements, a typical worst case may be that a recently resized dynamic array has allocated memory for 2n object references. 
        - With linked lists, memory must be devoted not only to store a reference to each contained object, but also to explicitly reference the link to the nodes. So a singly linked list of llength n ALREADY requires a 2n reference. 
    - Operations with equivalent asymptotic bounds typically run a constant factor more fficiently with an array vs a linked list. 
      - Consider the typical enqueue operation for a queue. Ignoring the issue of resizing an array, the operation for the ArrayQueue involves an arithmetic calculation of the new index, an increment of an integer, and storing a reference to the element in the array.
      - In contrast, the process for a linked node requires the instantiation of a node, appropriate linking of nodes, and an increment of an integer. While this operation completes in O(1) time in either model, the actual number of CPU operations will be more in the linked version, especially given the instantiation of the new node. 
- Advantages of Linked Lists:
    - Linked Lists provide a worst case time bound for their operations, in contrast to the amortized bounds of arrays. 
    - Linked Lists support O(1) time insertions and deletions at arbitrary positions. 
        - This is in stark contrast to an array based sequence. Ignoring the issue of resizing an array, inserting or deleting an element from the end of an array based list can be done in constant time.
        - However, more general insertions and deletions are expensive. 
"""
# Example of a Linked List


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# Printing the elements of a linked list:


def printLinkedList(head):
    current = head
    while current:
        print(current.data)
        current = current.next


# With head/current, etc, it doesn't matter if we're returning back node (after doing node.next = head), or returning head, because everything references the same list. Because we assign current = head, anything that we change in the current linked list will affect the head linked list, as they're the same list. What we're returning back (the head), is just there so we can have a reference to the head of the linked list as we traverse through it with current.
