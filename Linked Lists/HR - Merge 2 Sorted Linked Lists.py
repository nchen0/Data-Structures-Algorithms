# You’re given the pointer to the head nodes of two sorted linked lists. The data in both lists will be sorted in ascending order. Change the next pointers to obtain a single, merged linked list which also has data in ascending order. Either head pointer given may be null meaning that the corresponding list is empty.


def mergeLists(head1, head2):
    merged_node = SinglyLinkedList()

    while head1 and head2:
        if head1.data < head2.data:
            merged_node.insert_node(head1.data)
            head1 = head1.next
        else:
            merged_node.insert_node(head2.data)
            head2 = head2.next
    while head1:
        merged_node.insert_node(head1.data)
        head1 = head1.next
    while head2:
        merged_node.insert_node(head2.data)
        head2 = head2.next

    return merged_node.head
