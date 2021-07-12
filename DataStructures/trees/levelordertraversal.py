# def levelOrder(root):
#     if(root == None):
#         return
#     else:
#         depth = height(root)
#         for i in range(1, depth+1):
#             levelordertraversal (root, i)
            
# def height(root):
#     if(root == None):
#         return 0
#     else:
#         lheight = max(height(root.left),height(root.right))+1
#         return lheight
    
# def levelordertraversal(root, level):
#     if(root == None):
#         return
#     if(level == 1):
#         print(root.info, end= " ")
#     elif(level >1 ):
#         levelordertraversal(root.left, level-1)
#         levelordertraversal(root.right, level-1)

# using queue to print the level ordrer traversal 
 
  def levelordertraversal(root):
      if(root == None):
          return root
      else:
          queue = []
          queue.append(root)
          while(queue != None):
              current = queue.pop(0)
              print(current.value)
              if(current.left != None):
                  queue.append(root.left)
              if(current.right != None):
                  queue.append(root.right)