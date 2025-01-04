
class MinStack:

    def __init__(self):
        self.minstack = []
        self.minvalue_stack = [] 
        

    def push(self, val: int) -> None:
        self.minstack.append(val)

        if not self.minvalue_stack or val <= self.minvalue_stack[-1]:
            self.minvalue_stack.append(val)
        

    def pop(self) -> None:
        deleted_item = self.minstack.pop()
        if deleted_item == self.minvalue_stack[-1]:
            self.minvalue_stack.pop()
        
        

    def top(self) -> int:
        return self.minstack[-1]

        

    def getMin(self) -> int:
        return self.minvalue_stack[-1]


if __name__ == "__main__":

    teststack = MinStack()
    teststack.push(-2)
    teststack.push(0)
    teststack.push(-3)
    print(teststack.getMin())
    teststack.pop()
    print(teststack.top())
    print(teststack.getMin())


