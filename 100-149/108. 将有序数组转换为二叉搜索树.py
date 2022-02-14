'''
tc > 76%; sc > 71%
一次过，也是简单题，多解只需提交一种即可。看代码也好懂。
官方题解：基本和我一样。但它说sc为栈的深度=O(logn)，这怎么计算的？
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        le = len(nums)
        def cd(mi, ma) -> TreeNode:
            i = (mi+ma)//2
            root = TreeNode(nums[i])
            if mi == ma:
                return root
            if i > mi:
                root.left = cd(mi, i-1)
            root.right = cd(i+1, ma)
            return root

        return cd(0, le-1)

class Solution_first:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None: continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return res

class Solution_level:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res, sav = [[root],], [root]
        if not root:
            return []
        while sav:
            sav = []
            for i in res[-1]:
                if i.left:
                    sav.append(i.left)
                if i.right:
                    sav.append(i.right)
            res.append(sav)

        for i in range(len(res)-1):
            for j in range(len(res[i])):
                res[i][j] = res[i][j].val
        return res[:-1]

a = [_ for _ in range(1,7)]
print(Solution_first().inorderTraversal(Solution().sortedArrayToBST(a)))
print()
print(Solution_level().levelOrder(Solution().sortedArrayToBST(a)))
