def levelOrder(root):
    if(root == None):
        return
    else:
        depth = height(root)
        for i in range(1, depth+1):
            levelordertraversal (root, i)
            
def height(root):
    if(root == None):
        return 0
    else:
        lheight = max(height(root.left),height(root.right))+1
        return lheight
    
def levelordertraversal(root, level):
    if(root == None):
        return
    if(level == 1):
        print(root.info, end= " ")
    elif(level >1 ):
        levelordertraversal(root.left, level-1)
        levelordertraversal(root.right, level-1)


## another way to do this 
def levelOrder(root):
    if not root:
        return
    else:
        testqueue = [root]
        while len(testqueue)>0:
            poppednode = testqueue.pop(0)
            print(poppednode.info, end=" ")
            if poppednode.left:
                testqueue.append(poppednode.left)
            if poppednode.right:
                testqueue.append(poppednode.right)