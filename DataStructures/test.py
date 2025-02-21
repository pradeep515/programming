def insertionsort(nums):

    for i in range(1, len(nums)):
        j = i - 1
        key = list[i]
        while j >= 0  and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums
            



if __name__ == "__main__":

    list = [4,6,2,-1,9,55,33]
    print(insertionsort(list))

def topview (root):

    if not root:
        return None 
    
    hd = 0 
    node_dict = {} 
    queue.append((root, hd))
    while queue:

        node, hd = queue.popleft()
        if hd not in node_dict:
            node_dict[hd] = node 

        if node.left:
            queue.append((node.left,hd-1))

        if node.right:
            queue.append((node.right, hd+1))

    for key in sorted(node_dict.keys()):
        print(test_dict[key])











        

