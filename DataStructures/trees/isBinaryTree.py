
## check if a given tree is a binary search tree or not. condition is the left node value should be less than rootnode value less than right node value
def check_binary_search_tree_(root):
    def checkbst(root, min_value, max_value):
        if not root:
            return True
        if root.data < min_value or root.data > max_value:
            return False
        return (checkbst(root.left, min_value, root.data -1 ) and checkbst(root.right, root.data+1 , max_value))
    return checkbst(root, 0 , 10000)        