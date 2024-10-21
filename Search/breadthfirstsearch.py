graph = {"A":["B", "C"], 
'B': ['c']}  #python dictionary list of the nodes

queue = [] 
visited = set()

def bfs(node,graph, visited):
    visited.add(node)
    queue.append(node)
    while(queue):
        m = queue.pop()
        print (m)
        for neighbour in graph[m]:
            if(neighbour not in visited):
             queue.append(neighbour)
             visited.add(neighbour)

#another way to do it 
def BFS(head):
    if not head :
        return 
    testqueue = collections.dequeue();
    testqueue.append(head)
    while testqueue:
        node = testqueue.popleft()
        print (node.info)
        if node.left:
            testqueue.append(node.left)
        if node.right:
            testqueue.append(node.right)
             