# Given a pointer to the root of a binary tree, print the top view of the binary tree.
# The tree as seen from the top the nodes, is called the top view of the tree.

# just do a BFS and maintain the horizontal distance (distance from the root node) in a dict or map .

def topView(root):
   if not root:
       return
   else:
       testdict = {}
       testqueue = dequeue()
       hd = 0
       testqueue.append((head,hd))
       while(testqueue):
           node, hd = testqueue.popleft()
           if hd not in testdict:
               testdict[hd] = node
           if node.left:
               testqueue.append((node.left, hd-1))
           if node.right:
               testqueue.append((node.right, hd+1))
       return [testdict[hd] for hd in sorted(testdict.keys())] # this is just to return top view nodes based on the sorted hd values