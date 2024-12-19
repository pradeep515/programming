class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.minstack or val < self.minstack[-1]:
            self.minstack.append(val)
        

    def pop(self) -> None:
        poppedvalue = self.stack.pop()
        
        if poppedvalue == self.minstack[-1]:
            self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack)-1]
        

    def getMin(self) -> int: 
        return self.minstack[-1]
        


if __name__ == "__main__":
    teststack = MinStack()
    teststack.push(-2)
    teststack.push(0)
    teststack.push(-3)
    print(teststack.getMin())
    teststack.pop()
    print(teststack.top())
    print(teststack.getMin())
    




