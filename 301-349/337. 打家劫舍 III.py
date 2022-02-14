'''
执行用时：60 ms, 在所有 Python3 提交中击败了62.83%的用户
内存消耗：16.8 MB, 在所有 Python3 提交中击败了35.96%的用户
感觉只用了10-15分钟就解决掉的中等题。
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def cd(p:TreeNode):
            if not p:
                return (0,0)
            fleft, tleft = cd(p.left)
            fright, tright = cd(p.right)
            return (max(fleft, tleft)+max(fright, tright), p.val+fleft+fright)

        return max(cd(root))

root = TreeNode(3, TreeNode(4,TreeNode(1),TreeNode(3)), TreeNode(5,None,TreeNode(1)))
print(Solution().rob(root))