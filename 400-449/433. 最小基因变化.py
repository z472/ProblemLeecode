'''
210805 No.3

作者：powcai (力扣py提交大佬，学他好几篇了)
哇，这题目有点显而易见的感觉。就一个“图”式的算法题，可以BFS（最好吧）就不用DFS。
我不太会写说实话。我不太会BFS，而且DFS又常常陷入递归的泥潭。下面这个思路清晰，简洁的BFS
可以学习下。我之前有阵子写过一个类似的用队列的，貌似。这里又忘了，BFS适合用队列哦！再记一下。

值得注意的是他的子函数里用到了python生成器的技巧，这是叫作：惰性计算。可以节省空间。其实和
返回一个列表是一样的功效，但是不占空间。

BFS，队列，图。
'''
from typing import List
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        from collections import deque
        bank = set(bank)
        if end not in bank:
            return -1
        visited = set()
        visited.add(start)
        mutation = {"A", "C", "G", "T"}

        # 产生只差一个字母的基因
        def oneMutation(cur):
            for i, val in enumerate(cur):
                for t in mutation - {val}:
                    tmp = cur[:i] + t + cur[i + 1:]
                    if tmp in bank:
                        yield tmp

        queue = deque()
        queue.appendleft([start, 0])
        while queue:
            cur, res = queue.pop()
            if cur == end:
                return res
            for nxt in oneMutation(cur):
                if nxt not in visited:
                    visited.add(nxt)
                    queue.appendleft((nxt, res + 1))
        return -1

