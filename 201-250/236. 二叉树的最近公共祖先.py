'''
执行用时：72 ms, 在所有 Python3 提交中击败了92.40%的用户
内存消耗：28 MB, 在所有 Python3 提交中击败了11.48%的用户
这本来是写在235的代码，但我235看错题目了。
官方：
有递归和保存父结点两种方法。但tc和sc都一样为O(n)。看个速度更快的代码。它是64ms。其实就是看if条件的写法。或是有没有剪枝操作。
看上去它条件很朴素和简洁。我的就有点复杂了。
class Solution:
    def __init__(self):
        self.sums = 0

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==p or root==q:
            return root
        if root==None:
            return  None
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left==None and right==None:
            return None
        else:
            return left if left else right

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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