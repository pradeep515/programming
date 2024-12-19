
#    1) Divide the list in two parts - first node and 
#       rest of the linked list.
#    2) Call reverse for the rest of the linked list.
#    3) Link rest to first.
#    4) Fix head pointer


#reverse a linkedlist recursive
def reverse(head):
    if(head == None or head.next == None):
        return head
    else:
        reversedlist = reverse(head.next)
        head.next.next = head
        head.next = None
        return reversedlist


 # iterative solution   -- Take two pointers , Prev and nextnode
null-> 1 ->2->4->5-> null 
prev  head -> next node

  node prev = None
  node nextnode = None
  while(head!= None):
      nextnode = head.next
      head.next = prev
      prev = head
      head = nextnode.
  return prev 


  reverselinkedlist (head):
    prev = None 
    current = head 
    prev.next = current 
 

   while current:
      current.next, current ,prev = prev , current.next, current
      return prev

      