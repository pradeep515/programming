#  Construct Binary Tree from Preorder and Inorder Traversal
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not inorder or not preorder:
        return None
    rootval = preorder[0]
    root = TreeNode(rootval)

    rootindex = inorder.index(rootval)
    
    inorderleft = inorder[:rootindex]
    inorderright = inorder[rootindex+1:]

    preorderleft = preorder[1:len(inorderleft)+1]
    preorderright = preorder[len(inorderleft)+1:]

    root.left = self.buildTree(preorderleft, inorderleft)
    root.right = self.buildTree(preorderright, inorderright)

    return root