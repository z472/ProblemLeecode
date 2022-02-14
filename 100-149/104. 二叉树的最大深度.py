'''
版本一：
执行用时：60 ms, 在所有 Python3 提交中击败了13.85%的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了83.22%的用户
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res = 1
        sta = [root,]
        if not root:
            return 0
        while sta:
            sav = []
            for i in sta:
                if i.left:
                    sav.append(i.left)
                if i.right:
                    sav.append(i.right)
            sta = sav
            if sta:
                res += 1

        return res
版本二：
执行用时：56 ms, 在所有 Python3 提交中击败了27.96%的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了37.39%的用户
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0
官方题解：就是我的版本1,2的思路。下面复制了一份比我快了1/3的代码，tc击败96%的提交，是版本一的队列版本，双向队列
两边都可以增减，而且可以用for迭代，可以用位序，甚至可以限定大小，当在满员的时候在右边添加，左边会弹出，还有列表不
允许的insert(i, x)在i位置插入x。 加强版列表。 当然是在from collections import deque中的。
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 比我快1/3的提交，它就是和第一个提交一样的想法然后用deque（双向队列，append和pop的复杂度为O(1)）来实现的。

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        from collections import deque
        queue = deque()
        queue.append(root)
        depth = 0
        while len(queue) > 0:
            size = len(queue)
            for _ in range(size):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            depth += 1
        return depth



rl = TreeNode(2, TreeNode(3, None, TreeNode(7)), TreeNode(4))
rr = TreeNode(2, TreeNode(4), TreeNode(3, TreeNode(7), None))
root = TreeNode(1, rl, rr)
print(Solution().maxDepth(root))
