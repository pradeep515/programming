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