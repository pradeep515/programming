#remove nth node from a linked list in single pass 

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

    if not head:
        return head
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next