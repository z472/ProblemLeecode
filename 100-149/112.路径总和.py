'''
执行用时：60 ms, 在所有 Python3 提交中击败了19.15%的用户
内存消耗：16.7 MB, 在所有 Python3 提交中击败了10.30%的用户
简单题，一次过。但是这个表现让我笑出了声。第一次使用双向队列，也仅仅做了初始化，右加左减，len等基础操作。
官方题解：1.广度优先搜索+队列实现 看下它的表现tc = 48ms > 83%, sc = 16.7mb > 11%.居然会差这么多的？
稍微修改下写法，快1/4 ？？？ 这种一趟循环和嵌套循环走一样数量的代码之前在1-50有个“含义丰富”的题解。里面就是
这种情况，一趟不好想但是简洁速度也更快，现在看来。以后再遇到这样的，绝不写嵌套循环。这绝对是一个值得优化的点。
    2，迭代。
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        que_node = collections.deque([root])
        que_val = collections.deque([root.val])
        while que_node:
            now = que_node.popleft()
            temp = que_val.popleft()
            if not now.left and not now.right:
                if temp == sum:
                    return True
                continue
            if now.left:
                que_node.append(now.left)
                que_val.append(now.left.val + temp)
            if now.right:
                que_node.append(now.right)
                que_val.append(now.right.val + temp)
        return False
'''
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        d1, d2 = deque(), deque()
        d1.append(root)
        d2.append(targetSum - root.val)
        while len(d1):
            a = len(d1)
            for _ in range(a):
                i = d1[0]
                if i.left:
                    d1.append(i.left)
                    d2.append(d2[0] - i.left.val)
                if i.right:
                    d1.append(i.right)
                    d2.append(d2[0] - i.right.val)
                if not i.left and not i.right and d2[0] == 0:
                    return True
                d1.popleft()
                d2.popleft()

        return False


rl = TreeNode(2, TreeNode(3, None, TreeNode(7)), TreeNode(4))
rr = TreeNode(5, TreeNode(14), TreeNode(13, TreeNode(17), TreeNode(10)))
root = TreeNode(1, rl, rr)
mt = [7, 8, 13, 20, 36, 50]
for i in mt:
    print('in:', i)
    print(Solution().hasPathSum(root, i))
