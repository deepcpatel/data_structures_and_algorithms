# Link: https://leetcode.com/problems/min-stack/

# Approach: Create two stacks, one for storing input values and one for storing min_values until that state
# As you pop input values put, pop the corresponding min values, as they may no longer be available in input stack

class MinStack(object):
    
    def __init__(self):
        self.val_stack = []
        self.min_stack = []
        self.mini = float('inf')

    def push(self, x):
        self.val_stack.append(x)        
        
        if self.mini > x:
            self.mini = x
        self.min_stack.append(self.mini)
        
    def pop(self):
        self.val_stack.pop()
        self.min_stack.pop()
        
        if len(self.min_stack) == 0:
            self.mini = float('inf')
        else:
            self.mini = self.min_stack[-1]
        
    def top(self):
        return self.val_stack[-1]
        
    def getMin(self):
        return self.mini
    
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()