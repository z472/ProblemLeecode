'''
执行用时：316 ms, 在所有 Python3 提交中击败了59.10%的用户
内存消耗：19.3 MB, 在所有 Python3 提交中击败了5.01%的用户
通过测试用例：71 / 71

效率很低，但窃喜通过了，因为自己设置的递归返回值很容易出错，递归终结条件有超过4种的情况，其中有的语句
还包括多种情况输出，加上这题是二叉树的测试用例（力扣显示一个列表，我不好构造同样的二叉树），能通过确实
是窃喜。    看了题解，又学到了，递归函数使用一个全局变量简化了递归逻辑。下面是官方题解：
class Solution(object):
    def longestUnivaluePath(self, root):
        self.ans = 0

        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans

这个递归除了用个全局变量作为记录历史最长路径，而我的递归是到最后最大值是会保存在回退到根节点的。
官方题解也没有第二种别的方法，这题确实很容易想到的是递归，我递归经常就是写复杂了，之前也有个题。
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def child(node: TreeNode):
            a,b,c,d = 0,0,0,0
            r1, r2 = 0,0
            if not node:
                return (0, 0)
            if node.left:
                a,b = child(node.left)
                if node.val == node.left.val:
                    r1, r2 = a + 1, b
                else:
                    r1, r2 = 0, max(a, b)
            if node.right:
                c,d = child(node.right)
                if node.val == node.right.val:
                    r1, r2 = max(r1, c+1), max(r2, d)
                else:
                    r2 = max(r2, c, d)
            if node.left and node.right and node.val == node.left.val == node.right.val:
                r2 = max(a + c + 2, r2)
            # r1:以node结点为一端的最长路径，r2:其他情况的最长路径
            return (r1, r2)
        return max(child(root))

