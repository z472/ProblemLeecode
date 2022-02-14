'''
执行用时：64 ms, 在所有 Python3 提交中击败了73.45%的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了5.43%的用户

题目说是线性结构的循环队列，我不知道我怎么占用内存多了，这题错误了三次，第一次是加入第一个元素后的
队首、队尾索引设置错误，第二次是删除一个元素后的队首索引设置错误，第三次是获取队尾值错误(低级)。
'''
class MyCircularQueue:

    def __init__(self, k: int):
        self.mq = [ -7 for _ in range(k)]
        self.fr = self.rr = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            # 注意为空时添加的差异
            if not self.isEmpty():
                self.rr = (self.rr+1)%len(self.mq)
            self.mq[self.rr] = value
            return True
        return False

    def deQueue(self) -> bool:
        if self.Front() != -1:
            # 设置为初始值-7表示该位置放空
            self.mq[self.fr] = -7
            # 仅有一个元素时有区别
            if self.fr != self.rr:
                self.fr = (self.fr+1)%len(self.mq)
            return True
        return False

    def Front(self) -> int:
        return -1 if self.mq[self.fr] == -7 else self.mq[self.fr]

    def Rear(self) -> int:
        return self.mq[self.rr] if self.mq[self.rr] != -7 else -1

    def isEmpty(self) -> bool:
        return  self.Front() == -1

    def isFull(self) -> bool:
        return  self.fr == (self.rr+1)%len(self.mq) and self.Front() != -1