# Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

# Input: root = [4,2,5,1,3], target = 3.714286, k = 2
# Output: [4,3]

def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
    
    
    max_heap = [] 
    result = []
    
    def inorder(root):
        if not root:
            return 
        
        if root.left:
            inorder(root.left)
        heapq.heappush(max_heap,(-abs(target-root.val), root.val))
        if len(max_heap) > k :
            heapq.heappop(max_heap)
            
        if root.right:
            inorder(root.right)
            
    inorder(root)
    for _, val in max_heap:
        result.append(val)
    return result