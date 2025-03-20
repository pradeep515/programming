from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1: Build the graph
        graph = defaultdict(dict)
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1.0 / value
        
        # Step 2: DFS to compute division
        def dfs(start: str, end: str, visited: set) -> float:
            # If start or end not in graph, no path possible
            if start not in graph or end not in graph:
                return -1.0
            # If start == end, return 1.0
            if start == end:
                return 1.0
            # Mark current node as visited
            visited.add(start)
            # Explore neighbors
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return weight * result
            return -1.0
        
        # Step 3: Process each query
        results = []
        for start, end in queries:
            results.append(dfs(start, end, set()))
        
        return results