from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 由颜色标记，即那个倒着放入栈中的遍历算法。来的，先序遍历，因为过程只有一个，就不需要不同颜色的标记了。
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

# 改动标记法的后序遍历,只需要改white中代码的位置即可完成。万物起源的代码。
class Solution_end:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((GRAY, node))
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

root = TreeNode(2, TreeNode(3, TreeNode(1), TreeNode(6)), TreeNode(4, TreeNode(5), TreeNode(9)))
print(Solution_end().inorderTraversal(root))