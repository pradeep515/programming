
Given the pointer to the head node of a doubly linked list, reverse the order of the nodes in place. That is, change the next and prev pointers of the nodes so that the direction of the list is reversed. Return a reference to the head node of the reversed list.

Note: The head node might be NULL to indicate that the list is empty.

def reverse(llist):
        currentnode = llist
        head = currentnode
        while(currentnode != None and currentnode.next != None):
            tempnode = currentnode.prev
            currentnode.prev = currentnode.next
            currentnode.next = tempnode
            currentnode = currentnode.prev
        currentnode.next = currentnode.prev
        currentnode.prev = None
        return currentnode