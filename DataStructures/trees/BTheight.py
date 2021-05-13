# The height of a binary tree is the number of edges between the tree's root and its furthest leaf. For example, the following binary tree is of height 
def height(root):
    if(root == None):
        return -1
    else:
       return max(height(root.left), height(root.right)) + 1 