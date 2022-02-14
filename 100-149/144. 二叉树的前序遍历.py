'''
执行用时：36 ms, 在所有 Python3 提交中击败了82.36%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了47.87%的用户
之前95+的代码。就是前序遍历嘛。
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None: continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return res
