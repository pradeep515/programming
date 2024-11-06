import heapq

# li = [3,5,12,21,11]
# heapq.heappush(li,56)
# print(heapq.heappop(li))
# print(li)


def kthlargest(list, k):
    min_heap = []
  #checking if the size of the min_heap is greater than k , if so, 
            # remove the root(lowest value in priority queue). by doing this , kth element will be at the root by the end of hte loop
    for i in list:
        heapq.heappush(min_heap, i)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

def kthsmallest(list, k):
    max_heap = []  
    for i in list:
        heapq.heappush(max_heap, -i)
        if len(max_heap) > k :
            heapq.heappop(max_heap)
    return -max_heap[0]

if __name__== '__main__':
    list = [3,1,5,12,2,11]
    print(kthlargest(list,3))
    print(kthsmallest(list,4))
