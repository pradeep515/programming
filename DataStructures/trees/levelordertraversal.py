
    
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


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return [] 

        lqueue = deque()
        lqueue.append([root])
        resultqueue = []

        while lqueue:
            level = []
            levelsize = len(lqueue)

            for _ in range(levelsize):
                Node = lqueue.popleft()
                level.append(Node.val)

                if Node.left:
                    lqueue.append(Node.left)
                if Node.right:
                    lqueue.append(Node.right)
            resultqueue.append(level)
            
        return resultqueue