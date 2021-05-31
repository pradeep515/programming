
# Given the pointer to the head node of a doubly linked list, reverse the order of the nodes in place. That is, change the next and prev pointers of the nodes so that the direction of the list is reversed. Return a reference to the head node of the reversed list.

# Note: The head node might be NULL to indicate that the list is empty.

def reverse(llist):
        currentnode = llist
        head = currentnode
        while(currentnode != None and currentnode.next != None):
            previous = currentnode.prev    #save the previous pointer before pointing  currentnode.prev to next 
            currentnode.prev = currentnode.next
            currentnode.next = previous
            currentnode = currentnode.prev    # traverse in back because it has be reversed.
        previous = currentnode.prev  # explicitly move the previous since the currentnode is null to point to the first node. 
        head = previous
        return head 