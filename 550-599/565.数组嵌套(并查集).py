'''
执行结果：
执行用时：800 ms, 在所有 Python3 提交中击败了6.21%的用户
内存消耗：38.6 MB, 在所有 Python3 提交中击败了9.65%的用户

这不是tc,sc= O(n)的复杂度吗，怎么这么慢。。。

有一说有一，这题没有利用到题目内部的逻辑，反而是用并查集的强大功能去解决了。
这题也是一个有点逻辑判断的题，之前总想的是别的nums[i]进入之前遍历过的一个循环，却没有考虑到
nums中的值是唯一的，不存在那种情况。也就是每个循环都不会其他入口。只要标记访问过的话就可以结束，
获取一个循环长度作为返回值。  我也很奇怪，并查集究竟怎么利用了题目的这个不能访问之前访问到的要求。
我只用到了跳转这个要求嘛，这么看 不能访问之前结点 像是 跳转的一个延伸要求，可以没有，没有的话就是
无限循环了嘛。 速度不快很好理解，它有860多测试用例，而且使用并查集创建就会占用不少时间。
'''
from typing import List
class Node:
    def __init__(self, val, sums=1, dir=None):
        self.val = val
        self.sums = sums
        self.dir = dir

    def search(self):
        t1 = self
        while t1.dir:
            t1 = t1.dir
        return t1

    @staticmethod
    def union(p1, p2):
        r1, r2 = p1.search(), p2.search()
        if r1 != r2:
            if r1.sums > r2.sums:
                r1, r2 = r2, r1
            r1.dir = r2
            r2.sums += r1.sums


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        l1 = [Node(i) for i in nums]
        for idx in range(len(nums)):
            # if not l1[idx].dir:
            Node.union(l1[idx], l1[l1[idx].val])
        resmax = 0
        for i in l1:
            resmax = max(i.sums, resmax)
        return resmax

errors = [[1,2,3,4,5,0],]
for i in errors:
    print(Solution().arrayNesting(i))
