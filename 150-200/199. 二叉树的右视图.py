'''
执行用时：44 ms, 在所有 Python3 提交中击败了44.15%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了70.52%的用户
广度优先方法，tc,sc=O(n)
官方题解：深度优先更难写一些。
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rightmost_value_at_depth = dict() # 深度为索引，存放节点的值
        max_depth = -1

        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()

            if node is not None:
                # 维护二叉树的最大深度
                max_depth = max(max_depth, depth)

                # 如果不存在对应深度的节点我们才插入
                rightmost_value_at_depth.setdefault(depth, node.val)

                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]

'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        savline = [root]
        if not root:
            return None
        while savline:
            s = []
            res.append(savline[-1].val)
            for i in savline:
                if i.left:
                    s.append(i.left)
                if i.right:
                    s.append(i.right)
            savline = s
        return res

left = TreeNode(2, TreeNode(6,TreeNode(9, None, TreeNode(10))), TreeNode(7, None, TreeNode(8)))
right = TreeNode(3, TreeNode(4))
root = TreeNode(1, left, right)
print(Solution().rightSideView(root))