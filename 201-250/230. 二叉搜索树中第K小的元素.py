'''
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right

为何会有含义如此丰富的代码？该怎么写出这样看似错误的代码？
绝对的艺术代码。这代码之前我也有偶然写过，主要的特征就是它其实是一条条路径，“巧合”之处就是它把不同的逻辑
折叠藏在了代码的同样的路径中。
·感觉比较有可能的情况是，观察代码表意和各个条件。具体做法很有可能是先写出几个不同路径，然后观察出可以  共享  的地方合并不同路径。
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 借助之前中序遍历改的，自己不会写这么  浓缩  的代码。
        stack = [(root, 0)]
        node, tag = root, 0
        while k != 0:
            node, tag = stack.pop()
            if node is None: continue
            if tag == 0:
                stack.append((node.right, 0))
                stack.append((node, 1))
                stack.append((node.left, 0))
            else:
                k -= 1
        return node.val


root = TreeNode(3, TreeNode(0, None, TreeNode(2, TreeNode(1))))
print(Solution().kthSmallest(root, 4))
