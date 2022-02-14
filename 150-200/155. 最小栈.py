'''
没仔细看题目，top()不是弹出最小元素而是弹出栈顶元素。导致出现误解，以为要用双向队列来做。
难的点就只有随时获取最小值了。官方题解的思路是：建立个“辅助栈”，和原来栈同步操作的栈空间。记录最小元素位序。
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
'''