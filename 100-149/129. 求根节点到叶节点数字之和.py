'''
执行用时：28 ms, 在所有 Python3 提交中击败了99.15%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了84.76%的用户
写了和没写没啥区别。  官方题解：使用广度优先搜索，需要维护两个队列，分别存储节点和节点对应的数字。
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = []
        aggregate = 0

        def cd(p: TreeNode, s: str = '') -> None:
            if p.left:
                cd(p.left, s + str(p.val))
            if p.right:
                cd(p.right, s + str(p.val))
            if not p.left and not p.right:
                res.append(s + str(p.val))
                return

        cd(root)
        for i in res:
            aggregate += int(i)
        return aggregate

rl, rr = TreeNode(2,TreeNode(3), TreeNode(4)), TreeNode(6, TreeNode(7))
root = TreeNode(1, rl, rr)
print(Solution().sumNumbers(root))
