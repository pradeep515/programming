# Given pointers to the head nodes of  linked lists that merge together at some point, find the node where the two lists merge. The merge point is where both lists point to the same node, i.e. they reference the same memory location. It is guaranteed that the two head nodes will be different, and neither will be NULL. If the lists share a common node, return that node's  value.
# Note: After the merge point, both lists will share the same node pointers.

def findMergeNode(head1, head2):
    current1 = head1
    current2 = head2
    head1length=0
    head2length=0
    while(head1!= None):
        head1length =head1length + 1
        head1 = head1.next
    while(head2!= None):
        head2length =head2length + 1
        head2 = head2.next
    equalpoint = abs(head2length-head1length)
    i = 0
    j = 0 
    if(head1length > head2length):
        while(i< equalpoint and current1!= None):
            current1 = current1.next
    else:
        while(j< equalpoint and current2!= None):
            current2 = current2.next
        
    while(current1 != None and current2 != None):
        if(current1 == current2):
            return current1.data
        else:
            current1 = current1.next
            current2 = current2.next
    return 0
    