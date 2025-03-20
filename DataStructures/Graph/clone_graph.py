class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    if not node:
        return None
    
    # Hash map to store the cloned nodes
    visited = {}
    
    def dfs(node):
        # If node already cloned, return the clone
        if node in visited:
            return visited[node]
        
        # Create clone of current node
        clone = Node(node.val)
        # Mark as visited with its clone
        visited[node] = clone
        
        # Recursively clone all neighbors
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone
    
    return dfs(node)