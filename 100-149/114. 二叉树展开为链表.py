'''
执行用时：36 ms, 在所有 Python3 提交中击败了96.08%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了85.79%的用户
虽然是第二次过的，但是第一次是漏个小逻辑很快改好了。这题解的感觉很享受。递归代码省略的地方也有在表达逻辑，if的条件写的
也是有顺序有含义的，所以看起来很简洁。表现也很棒。但仔细看由于我要把左链表的尾巴给接到该结点的右子链表头上，需要再遍历
左链表下去，导致重复经过某个结点。       官方题解三，它通过--找前置结点的办法来设计了一个tc=O(n),sc=O(1)的东西
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        # 递归返回上层该结点是否成功展开为链表
        if not root:
            return None

        def cd(p) -> bool:
            t = p.left

            if p.left and cd(p.left):
                while t.right:
                    t = t.right
            # 顺序不能变
            if ((p.right and cd(p.right)) or not p.right) and p.left:
                t.right = p.right
                p.right = p.left
                p.left = None

            return True

        cd(root)
        return root


rl = TreeNode(1, TreeNode(9), TreeNode(2))
rr = TreeNode(5, TreeNode(4), TreeNode(6))
# root = TreeNode(3, rl, rr)
root = TreeNode(1, TreeNode(2))
p = Solution().flatten(root)
while p:
    print(p.val, end=' ')
    print(p.left, end=' ')
    p = p.right
