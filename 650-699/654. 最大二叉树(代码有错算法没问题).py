'''
回归学习的一个题，分析，解的什么东西。官方的意思就是递归，然后用编程语言的findmax函数，因为说了是
无重复值（题目重复值也没法编了）的。python就可以是nums.index(max(nums[l:r]))。然后按题目
描述去递归就好了。这相当于是蛮力法了。tc=O(nlogn)，最坏n^2     我想的方法是结合单调栈，一次遍历
tc=O(n)。显然是不对的（官方不可能解法要比我的差）。       我的算法，看下面代码，就两种情况，流水
账代码。当测试用例来到No.7时候会超时，也不知道是怎么回事。都不是输出错，是运行错。     这个算法的逻辑
错在哪呢？反正我也不确定它对在哪里。

概括的讲，我只对相邻的数值关系做了一些结点的排列。
https://leetcode-cn.com/problems/maximum-binary-tree/solution/zui-da-er-cha-shu-di-gui-he-fei-di-gui-o-5fde/
找到一个题解里面讲的 非递归O(n)也是单调栈实现，但没细看，哎，有点想游戏
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        head = TreeNode(nums[0])
        # 单调栈保存的是降序的，右节点序列，它们可能会被置为新增结点的左结点，从而出栈
        stack = [head]
        lastnode = None
        for idx in range(1, len(nums)):
            while True:
                i = TreeNode(nums[idx])
                if nums[idx] < stack[-1].val:
                    i.left = lastnode
                    stack[-1].right = i
                    stack.append(i)
                    break
                else:
                    lastnode = stack.pop()
                    if not stack:
                        i.left = lastnode
                        lastnode = None
                        head = i
                        stack.append(i)
                        break
        return head
