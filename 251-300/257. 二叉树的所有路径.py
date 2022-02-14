'''
tc > 97%, sc > 93%。简单题。
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        ret = []
        a, b = self.binaryTreePaths(root.left), self.binaryTreePaths(root.right)
        if not a and not b:
            return [str(root.val)]
        for i in a + b:
            ret.append(str(root.val)+'->'+i)
        return ret

root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(8, TreeNode(6)))
print(Solution().binaryTreePaths(root))