'''
通过测试用例：
77 / 78
这个报错是测试用例low,high都为35，且是一个很大的二叉搜索树，要是手动根据力扣的列表构造二叉搜索树就很迷。
我的输出的根节点为35左子树为空，右子树为36.正确答案应该为35，左右子树皆为空。
这应该是我算法的漏洞，大方向上应该没问题，但是小细节可能有问题。

官方题解是递归。代码很少
class Solution(object):
    def trimBST(self, root, L, R):
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def prune(node: TreeNode, i: int, low, high) -> TreeNode:
            # 修剪最大or小值
            tag = (i == low)
            stack = []
            # 遍历，保存符合一个边界的结点
            while node:
                nval = node.val
                if low <= nval <= high:
                    stack.append(node)
                # bug一次，然后归纳，整合，缩减写法
                node = node.right if nval < i or (not tag and nval == i) else node.left
            # 连接

            for i in range(len(stack) - 1):
                if stack[i].val > stack[i + 1].val:
                    stack[i].left = stack[i + 1]
                else:
                    stack[i].right = stack[i + 1]
            if stack:
                if tag:
                    stack[-1].left = None
                else:
                    stack[-1].right = None
            return stack[0] if stack else None

        root = prune(root, low, low, high)
        return prune(root, high, low, high)

r1 = TreeNode(3, TreeNode(0, None, TreeNode(2, TreeNode(1))), TreeNode(4))
r2 = Solution().trimBST(r1, 1, 3)
print('end')
