from collections import deque
testqueue = deque()
testqueue.append(1)
testqueue.append(333)
testqueue.append(42)
testqueue.append(54)
testqueue.append(63)
print(testqueue)
testqueue.popleft()
print(testqueue)
testqueue.rotate()
print (testqueue)

