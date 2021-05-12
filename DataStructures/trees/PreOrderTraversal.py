def preOrder(root):
    #Write your code here
    if(root == None):
        return
    else:
        print(root.info , end =" ")
        if(root.left != None):
            preOrder(root.left)
        if(root.right != None):
            preOrder(root.right)