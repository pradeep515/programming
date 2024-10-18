# Using a Python dictionary to act as an adjacency list
from collections import deque
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}



visted = set()

def dfs(node, visited, graph):
    if(node not in visted):
        print (node)
        visted.add(node)
    for neighbour in graph[node]:
        if(neighbour not in visited):
            dfs(neighbour, visited, graph)

#another way 

def dfs(root):
    if not root:
        return
    else:
        stack = deque(root)
        while(stack):
            node = stack.pop()
            print(node.info)
            if (node.right):
                stack.append(node.right)
            if (node.left):
                stack.append(node.left)