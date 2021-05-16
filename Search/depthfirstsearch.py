# Using a Python dictionary to act as an adjacency list
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