def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
    
    result = [] 
    
    def dfs(root):
        
        if not root : 
            return -1 
        
        left = dfs(root.left)
        right = dfs(root.right)
        
        current_height = 1 + max(left, right)
        
        if len(result) <= current_height:
            result.append([])
        result[current_height].append(root.val)
        
        return current_height
    
    dfs(root)
    return result