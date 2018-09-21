# You're given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order. Delete as few nodes as possible so that the list does not contain any value more than once. The given head pointer may be null indicating that the list is empty.


def removeDuplicates(head):
    current = head
    while current.next:
        print('current is: {}'.format(current.data))
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head
