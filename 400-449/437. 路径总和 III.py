'''
这道题好气啊，难度都在编码的细节上，最离谱的是我的nonlocal值，从输出的id(res)可以明白
函数内用的res是它值，但修改的不是它原本的值。

再说说我的解法，和网友们大多的解法：前缀和相比。要占用更多的空间。
我是自底向上，他们是自上而下。到一个地方就计算一下。嗯。
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        global res
        res = 0
        def child(curNode):
            global res
            left = right = []
            if curNode.left:
                left = child(curNode.left)
            if curNode.right:
                right = child(curNode.right)
            if not curNode.left and not curNode.right:
                return [curNode.val]
            c = left+right
            if curNode == root:
                print('root:', c)
            res += c.count(targetSum)
            print(res, id(res))
            return [i+curNode.val for i in c]+[curNode.val]
        res += child(root).count(targetSum)
        print(id(res))
        return res

left = TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1)))
right = TreeNode(-3, None, TreeNode(11))
root = TreeNode(10, left, right)
print(Solution().pathSum(root, 8))
