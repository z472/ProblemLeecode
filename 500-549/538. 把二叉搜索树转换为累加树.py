# 执行用时：44 ms, 在所有 Python3 提交中击败了99.78%的用户
# 内存消耗：17.2 MB, 在所有 Python3 提交中击败了62.10%的用户
# 思路就是右侧的中序遍历，因为它的累加树是从右向左累加，所以用一个res去维护，
# 别老写错你想指代的变量好吧，还有就是注意对空值的屏蔽。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root):
        if not root:
            return None
        stack = [[root,0]]
        res = 0
        while stack:
            end = stack[-1]
            if end[1] == 0:
                if end[0].right:
                    stack.append([end[0].right,0])  # bug1加入[root.right, 0]喝假酒了吗
                end[1] = 1
            else:
                res += end[0].val
                end[0].val = res
                node = stack.pop()
                if node[0].left:
                    stack.append([node[0].left, 0]) #bug2,是0不是1
        return root





test = TreeNode(4, TreeNode(1,TreeNode(0), TreeNode(2,None,TreeNode(3))), TreeNode(6,TreeNode(5), TreeNode(7,None,TreeNode(8))))
r= Solution().convertBST(test)
print(r)
