class MinStack:

    def __init__(self):
        self.stack = []
        self.MinStack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if not len(self.MinStack) == 0:
            cur_min = self.MinStack[len(self.MinStack)-1]
            if val < cur_min: 
                self.MinStack.append(val)
            else:
                self.MinStack.append(cur_min)
        else:
            self.MinStack.append(val)

        
        

    def pop(self) -> None:
        self.stack.pop()
        self.MinStack.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.MinStack[len(self.MinStack)-1]
        




#leetcode stuff
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()