'''
执行用时：92 ms, 在所有 Python3 提交中击败了42.77%的用户
内存消耗：17.3 MB, 在所有 Python3 提交中击败了5.25%的用户

这题的输出条件太简单了，居然也是中等题
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        pre = p = root
        while p:
            pre = p
            if p.val < val:
                p = p.right
                if not p:
                    pre.right = TreeNode(val)
            else:
                p = p.left
                if not p:
                    pre.left = TreeNode(val)
        return root if root else TreeNode(val)
