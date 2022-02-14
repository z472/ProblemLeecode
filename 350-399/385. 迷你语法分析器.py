'''
这题麻烦在理解题意和题目所给类NestedInteger的几个函数。有的是对题目没有什么帮助的。当我看完英文注解。
然后就是一个字符串转化的问题。

我是10分钟编码完成，5分钟改了一个bug。而且是全在力扣上完成的。因为我不知道
它的NestedInteger是怎么写的。有可能和我理解不一样，像之前有个题一样。之所以编的这么快是我发现了它一些
问题的逻辑。其实难点也就是一个 栈，单词是怎么实现的，各个字符对应的操作之类的。

这种题是用递归和不用其实是一样的，我觉得还是模拟栈来写要更省内存些，也会更有价值些。

在这个速度来讲我很满意。
'''
# 题目里给的一个类，要我们根据它的接口来编码。
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        pass

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        pass


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = []
        length = 0
        for idx, i in enumerate(s):
            if i == '[':
                stack.append(NestedInteger())
            elif '0' <= i <= '9' or i == '-':
                length += 1
            elif i in [',', ']']:
                if length > 0:
                    stack[-1].add(NestedInteger(int(s[idx - length:idx])))
                length = 0
                if i == ']' and len(stack) > 1:
                    stack[-2].add(stack[-1])
                    stack.pop()
        return stack[0] if stack else NestedInteger(int(s))
