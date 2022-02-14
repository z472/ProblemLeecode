'''
执行用时：128 ms, 在所有 Python3 提交中击败了5.98%的用户
内存消耗：18.8 MB, 在所有 Python3 提交中击败了65.61%的用户
没看到说的是二叉搜索树。我这个是随便一个二叉树的随便两个结点的最近共同祖先。
官方：一次遍历，用二叉搜索树的特性走的。

'''


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ret = None

        def cd(root: TreeNode):
            nonlocal ret
            if not root or ret:
                return None
            p1, p2 = cd(root.left), cd(root.right)  # 先做子结点
            if (root in [p, q] and (p1 or p2)) or (p1 and p2):
                ret = root
            elif root in [p, q] or (p1 or p2):
                return True

        cd(root)
        return ret


q = TreeNode(9)
p = TreeNode(2, TreeNode(0), TreeNode(4))
root = TreeNode(6, p, TreeNode(8, TreeNode(7), q))
print(Solution().lowestCommonAncestor(root, p, q).val)
