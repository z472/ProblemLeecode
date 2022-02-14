from collections import deque


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.先序遍历
        """
        if not root:
            return ''
        res = ''
        d1 = deque([root])
        while d1:
            node = d1.pop()
            if node:
                res += str(node.val) + '|'
                d1.extend([node.right, node.left])
        return res.rstrip('|')

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return
        TNodes = [TreeNode(int(i)) for i in data.split('|')]
        root = TNodes[0]
        stack = [root]
        for node in TNodes[1:]:
            if node.val < stack[-1].val:
                stack[-1].left = node
                stack.append(node)
            else:
                while True:
                    if stack and stack[-1].val < node.val:
                        last = stack.pop()
                    else:
                        last.right = node
                        break
                stack.append(node)
        return root

right = TreeNode(9,TreeNode(8,TreeNode(7)))
left = TreeNode(6, TreeNode(1, None, TreeNode(5)), right)
root = TreeNode(10, left)
print(Codec().serialize(root))
data = Codec().serialize(root)
root_new = Codec().deserialize(data)
print(Codec().serialize(root_new) == data)
