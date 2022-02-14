'''
执行用时：44 ms, 在所有 Python3 提交中击败了57.21%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了58.74%的用户
一次过。这是简单难度。速度有点慢。题目推荐用到递归和迭代两种方法。递归方法没想通，迭代就常规来写。官方题解
里递归的写法是参数为左右两个指针，逻辑是同时移动两个指针，比较当前的值，左树向左，同时右树向右。一直想不通
怎么把两个树的结点同时比较。  是因为没发现同时比较的正确逻辑，每个树的右子树都与另一个树的左子树镜像对称。
当然做完左边的还有右侧的递归。官方没有py3版本，这是一个网友的代码,36ms用时，但他没有处理第一个根节点，导
致它子函数的return会把递归重复做一遍，子函数逻辑是需要那么写的，但它如果root是一个对称的树，它代码就是要
做两次。
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def checkSym(node1,node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            if node1.val!=node2.val:
                return False
            return checkSym(node1.left,node2.right) and checkSym(node1.right,node2.left)
        return checkSym(root,root)
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        st1, st2 = [root.left], [root.right]
        while st1 or st2:
            a, b = st1.pop(), st2.pop()
            # 不符合对称的情况
            if not a and not b:
                continue
            elif (not a or not b) or (a.val != b.val):
                return False
            if a:
                st1 += [a.right, a.left]
                st2 += [b.left, b.right]
        return True


rl = TreeNode(2, TreeNode(3, None, TreeNode(7)), TreeNode(4))
rr = TreeNode(2, TreeNode(4), TreeNode(3, TreeNode(7), None))
rl1 = TreeNode(2, None, TreeNode(3))
root = TreeNode(1, rl1, rl1)
print(Solution().isSymmetric(root))