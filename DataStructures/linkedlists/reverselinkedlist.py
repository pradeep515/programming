
#    1) Divide the list in two parts - first node and 
#       rest of the linked list.
#    2) Call reverse for the rest of the linked list.
#    3) Link rest to first.
#    4) Fix head pointer


#reverse a linkedlist
def reverse(head):
    if(head == None or head.next == None):
        return head
    else:
        rest = reverse(head.next)
        head.next.next = head
        head.next = None
        return rest