# 138. Copy List with Random Pointer

# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of 
# ts corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers 
# in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        current = head
        while current:
            new_node = Node(current.val, current.next, None)
            current.next = new_node
            current = new_node.next
        
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next 

        original = head 
        copy = head.next 
        new_head = head.next 
        
        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next

        return new_head