# You’re given the pointer to the head nodes of two linked lists. Compare the data in the nodes of the linked lists to check if they are equal. The lists are equal only if they have the same number of nodes and corresponding nodes contain the same data. Either head pointer given may be null meaning that the corresponding list is empty.


def compare_lists(llist1, llist2):
    isEqual = 1
    current1 = llist1
    current2 = llist2
    while current1 or current2:
        if current1 == None or current2 == None:
            isEqual = 0
            return isEqual
        print("current 1 is: {}".format(current1.data))
        print("current 2 is: {}".format(current2.data))
        if current1.data != current2.data:
            isEqual = 0
        current1 = current1.next
        current2 = current2.next

    return isEqual
