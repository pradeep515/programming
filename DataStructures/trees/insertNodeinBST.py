#insert a node into a binary search tree ( BST property is left child values are less than right child values)

def insert(root, key):
    # If the tree is empty, return a new node
    if root is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < root.data:
        root.left = insert(root.left, key)  # Insert in the left subtree
    else:
        root.right = insert(root.right, key)  # Insert in the right subtree

    return root  # Return the unchanged root pointer