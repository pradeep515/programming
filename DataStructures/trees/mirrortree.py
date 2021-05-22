# give a root node, mirror the tree ( the left and right childs should be swapped)

def mirrortree(root):
    if(root != None):
        mirrortree(root.left)
        mirrortree(root.right)
        root.left, root.right = root.right,root.left
    else:
        return
