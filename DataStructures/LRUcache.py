class Node:
    def __init__(self, key , value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next, self.tail.prev  = self.tail , self.head
    
    def add(self, node:Node):
        node.prev,node.next = self.head, self.head.next 
    def remove(self , node: Node):
        node.next.prev, node.prev.next = node.prev, node.next
    
    def get(self , key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.value
        else:
            return -1

    def put (self, key , value):
        if key in self.cache:
            del self.cache[key]
        if len(self.cache) > self.capacity:
            lrunode = self.tail.prev
            self.remove(lrunode)
        newnode = Node(key, value)
        self.cache[key] = newnode
        self.add(newnode)



    
    