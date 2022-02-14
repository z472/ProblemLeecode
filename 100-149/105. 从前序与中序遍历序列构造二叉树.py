'''
执行用时：92 ms, 在所有 Python3 提交中击败了70.95%的用户
内存消耗：19.2 MB, 在所有 Python3 提交中击败了83.16%的用户
一次过，代码很简洁，主要是第一次用这么多变量来解题，如果不是用这么多变量来做。你的思路就很混乱，编码的时候用一个
量和一个实际是在不断变动规则来试图分解出两个含义。主要还是从实例中整理出多个有区别的含义，即使是很细微的差别。这
和之前有些走路径多条件的那种拆分是一个道理。
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # mi, ma为下层可取到的中序列表的边界值，cur是前序遍历列表的位序, mi为当前值的前序遍历位序
        def child(cur, mi, ma) -> TreeNode:
            root, b = TreeNode(preorder[cur]), inorder.index(preorder[cur])
            if mi != b:
                root.left = child(cur + 1, mi, b - 1)
            if ma != b:
                root.right = child(cur + (b - mi) + 1, b + 1, ma)
            return root

        return child(0, 0, len(preorder) - 1)


class Solution_mid:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None: return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


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


mt1 = [[3, 9, 1, 2, 4, 20, 15, 17, 7, 13], [1, 9, 4, 2, 3, 15, 17, 20, 7, 13]]
mt2 = [[1, 2, 3, 4, 6], [2, 3, 1, 4, 6]]
mt3 = [[1, 2], [1, 2]]
i = mt2
print(Solution_first().inorderTraversal(Solution().buildTree(i[0], i[1])))
print(Solution_mid().inorderTraversal(Solution().buildTree(i[0], i[1])))
