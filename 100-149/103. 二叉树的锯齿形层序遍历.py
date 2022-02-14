'''
执行用时：40 ms, 在所有 Python3 提交中击败了65.72%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了18.27%的用户
第二次过的。且思路纯抄袭102层序遍历。就是在第二个循环里，把奇数行（从0行来算）的值相反的修改了。所以表现也很一般。
官方题解：居然和我完全一样的偷懒思路。
'''
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res, sav = [[root], ], 1
        if not root:
            return []
        while sav:
            sav = []
            for i in res[-1]:
                if i.left:
                    sav.append(i.left)
                if i.right:
                    sav.append(i.right)
            if sav:
                res.append(sav)

        for i in range(len(res)):
            b = len(res[i])
            if i % 2:
                for j in range(b//2):
                    res[i][j], res[i][b-1-j] = res[i][b-1-j].val, res[i][j].val
                if b % 2:
                    res[i][b // 2] = res[i][b // 2].val
            else:
                for j in range(b):
                    res[i][j] = res[i][j].val

        return res

rl = TreeNode(2, TreeNode(3, None, TreeNode(7)), TreeNode(4))
rr = TreeNode(5, TreeNode(14), TreeNode(13, TreeNode(17), TreeNode(10)))
root = TreeNode(1, rl, rr)
# root = TreeNode(1, TreeNode(2))
# Solution().zigzagLevelOrder(root)
for i in Solution().zigzagLevelOrder(root):
    print(i)