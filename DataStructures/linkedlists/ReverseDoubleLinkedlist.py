
# Given the pointer to the head node of a doubly linked list, reverse the order of the nodes in place. That is, change the next and prev pointers of the nodes so that the direction of the list is reversed. Return a reference to the head node of the reversed list.

# Note: The head node might be NULL to indicate that the list is empty.

#first way
def reverse(head):
    if not head:
        return head
    else:
        while head.next:
            head.next, head.prev, head = head.prev, head.next, head.next
        head.next, head.prev = head.prev, None
        return head
    
          while current :
           current.next, c.prev, current = prev, current.next, current.next
     current.prev = None
    
#second way 
def reverse(head):
    if not head:
        return head
    else:
        current = head
        while current:
            tmp = current.prev
            current.prev = current.next
            current.next = tmp
            current = current.prev
        if tmp:
            tmp = tmp.prev
        return tmp