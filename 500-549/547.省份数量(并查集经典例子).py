'''
执行用时：52 ms, 在所有 Python3 提交中击败了40.96%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了60.47的用户
'''
from typing import List
class Node:
    def __init__(self, val, sums=1, dir=None):
        self.val = val
        self.sums = sums
        # 指向的上层结点
        self.dir = dir
    # 查看操作，找结点的最终指向的根节点
    def search(self):
        t1 = self
        while t1.dir:
            t1 = t1.dir
        return t1
    # 合并操作，让结点少的指向结点多的集合，这里有个理解要点是：为何要连结这两个结点的根节点。
    # 合并连结一定是根节点间的操作，如果任意两个结点修改指向就会出现，1与2,4相连，先让1连到2上，
    # 再让1去连4，相当于舍弃了1,2相连的成果。我之前觉得不好理解，实际遇到要写又觉得不难理解，
    # 这是正确操作的唯一方法。
    @staticmethod
    def union(p1, p2):
        r1, r2 = p1.search(), p2.search()
        if r1 != r2:
            if r1.sums > r2.sums:
                r1, r2 = r2, r1
            r1.dir = r2
            r2.sums += r1.sums


class Solution:
    def findCircleNum(self, nums: List[List[int]]) -> int:
        le = len(nums[0])
        s = [Node(i) for i in range(le)]
        # 对nums[i][j] i<j的元素操作，矩阵右上方，表示要求出对指向node.val=i结点集合树
        # 每个nums[i][j]=1表示一次并和一次查操作，
        for i in range(le):
            for j in range(i+1, le):
                if nums[i][j] == 1:
                    Node.union(s[i], s[j])
        count = 0
        for si in s:
            if not si.dir:
                count += 1
        return count

# 没有测试过，直接提交一次过了