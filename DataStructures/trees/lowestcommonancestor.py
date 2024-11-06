def lca(root, v1, v2):
    if v1 > v2:
        v1, v2 = v2, v1
    while root:
        if root.info > v1 and root.info>v2:
            root = root.left
        elif root.info<v1 and root.info <v2:
            root = root.right
        else:
            return root
    return None