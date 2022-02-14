'''
执行用时：36 ms, 在所有 Python3 提交中击败了99.35%的用户
内存消耗：19.7 MB, 在所有 Python3 提交中击败了17.52%的用户
抿嘴，很一般的递归题，不知道哪里有价值能说。
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return []

        def cd(lt, p):
            a = sum(lt) + p.val
            if a == targetSum and not p.left and not p.right:
                res.append(lt + [p.val])
                return
            else:
                if p.left:
                    cd(lt + [p.val], p.left)
                if p.right:
                    cd(lt + [p.val], p.right)

        cd([], root)
        return res


rl = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
rr = TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))
root1 = TreeNode(5, rl, rr)
print(Solution().pathSum(root1, 22))

rl = TreeNode(2, TreeNode(3, None, TreeNode(7)), TreeNode(4))
rr = TreeNode(5, TreeNode(14), TreeNode(13, TreeNode(17), TreeNode(10)))
root = TreeNode(1, rl, rr)
