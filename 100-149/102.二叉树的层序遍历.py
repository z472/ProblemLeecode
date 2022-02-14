'''
执行用时：36 ms, 在所有 Python3 提交中击败了89.83%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了67.88%的用户
表现还不错，但是错了两次，第一次是输入[]，我输出了[[]];第二次是手抖删多了，然后提交出去语法错误。
官方题解：广度优先遍历的改版。好像就是你的解法。这题噱头比较大，思路和很多人的提交都是很顺利的。
'''
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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

rl = TreeNode(2, TreeNode(3, None, TreeNode(7)), TreeNode(4))
rr = TreeNode(2, TreeNode(4), TreeNode(3, TreeNode(7), None))
root = TreeNode(1, rl, rr)
for i in Solution().levelOrder(root):
    print(i)