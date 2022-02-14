'''
执行用时：36 ms, 在所有 Python3 提交中击败了81.21%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了31.89%的用户
迭代（非递归）是题目里要求的写法，依靠栈的存储和tag来表示下底遍历和回退两种状态，比较难的地方是细心
和回退部分。第一次错在了root为None，几乎就是一次过，本来也没什么特殊情况，就是下底，返回两种情况，
返回再细化出从左边返回，或是从右边返回两种情况再细化。递归版本在最后面的注释部分。递归版本也提交了速
度为40ms。        最大的问题是，你的代码的表达上还能不能再简短一点，你这个30行的代码太不python-
ic了。可以说是丑陋不堪。   官方题解：非递归版本有两个算法，一个是栈，一个是Morris中序遍历算法。后者
的时间虽然为O(n)，但它要遍历每个结点两次；但它不需要额外的空间。
官方题解：没有Python版代码，以下是一个py3的题解，非递归+栈，自称为颜色标记法，而且调整入栈顺序就可以
完成二叉树前后序遍历，且代码量是15行，我的一半。所以它的过程也很短，很易懂。这里它用大写两个变量来表示
常量，进而获得更为清楚的思路。
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res
再来一个32ms的提交代码，特别简洁。
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:return []
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        sta = []
        tag = 0  # 0为下底遍历，1为回退
        a = root
        if not root:
            return []
        if not root.left and not root.right:
            tag = 1
            res.append(a.val)
        while a != root or tag != 1:
            if tag == 0:
                sta.append(a)
                if a.left:
                    a = a.left
                elif a.right:
                    res.append(a.val)
                    a = a.right
                else:
                    tag = 1
            else:
                if not sta[-1].left and not sta[-1].right:
                    res.append(sta[-1].val)
                a = sta.pop()
                if sta[-1].left == a:  # 这里想用id()来确定地址，但是py语法特点就是这种容器类型是存的引用
                    res.append(sta[-1].val)
                    a, tag = (sta[-1].right, 0) if sta[-1].right else (sta[-1], 1)
                else:
                    a = sta[-1]
        return res


# 创建二叉树
# root = TreeNode(2, TreeNode(3, TreeNode(6), TreeNode(6)), TreeNode(4, TreeNode(5), TreeNode(5)))
root = TreeNode(3, )
Solution().inorderTraversal(root)
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return []

        def child(px):
            if px.left:
                child(px.left)
            res.append(px.val)
            if px.right:
                child(px.right)
            return

        child(root)
        return res
'''
