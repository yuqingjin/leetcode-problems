# Method1: stack 
# Basic idea: Pairing the value with the current stack minimum
# Method2: two stacks; maintain a decreasing order queue, a subsequence of the original one, keeping all the ele in decreasing order, deleting those not qualified ele.
# T: O(1)
# S:O(n)

# method 1
# class MinStack:

#     def __init__(self):
#         # pair the element and the current minimum
#         self.stack = []
#         self.min = inf
        
#     # push to the top of the stack -- the end of stack
#     def push(self, val: int) -> None:
#         if val < self.min:
#             self.min = val
#         self.stack.append((val, self.min))

#     def pop(self) -> None:
#         self.stack.pop()
#         if self.stack:
#             self.min = self.stack[-1][1]
#         else:
#             self.min = inf

#     def top(self) -> int:
#         if self.stack:
#             return self.stack[-1][0]

#     def getMin(self) -> int:
#         return self.min


# method2: two stacks
class MinStack:

    def __init__(self):
        self.stack = []
        self.decQ = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        # 两种情况
        # 此处等最小值的情况，也要append进decQ
        if not self.decQ or val <= self.decQ[-1]:
            self.decQ.append(val)

    def pop(self) -> None:
        cur = self.stack.pop()
        if self.decQ and self.decQ[-1] == cur:
            self.decQ.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.decQ:
            return self.decQ[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
