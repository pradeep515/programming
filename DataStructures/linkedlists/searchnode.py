Complete the getNode function in the editor below.

getNode has the following parameters:

SinglyLinkedListNode pointer head: refers to the head of the list
int positionFromTail: the item to retrieve

def getNode(llist, positionFromTail):
    head = llist
    if(llist == None):
        return llist
    else:
        length = 0
        while(llist != None):
            length = length +1
            llist = llist.next
        indextomove = length - positionFromTail -1
        i=0
        while(i<indextomove):
            head = head.next
            i =i +1
        return head.data
