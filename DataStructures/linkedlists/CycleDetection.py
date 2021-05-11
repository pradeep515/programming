A linked list is said to contain a cycle if any node is visited more than once while traversing the list. Given a pointer to the head of a linked list, determine if it contains a cycle. If it does, return . Otherwise, return .


def has_cycle(head):
    if(head == None):
        return 0
    else:
        currentnode = head
        jumpernode = head.next
        while(currentnode != None and jumpernode != None and jumpernode.next != None):
            if (currentnode == jumpernode):
                return 1;
            else:
                currentnode = currentnode.next;
                jumpernode  = jumpernode.next.next;
        return 0
            