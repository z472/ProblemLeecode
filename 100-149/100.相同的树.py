'''
执行用时：32 ms, 在所有 Python3 提交中击败了95.06%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了61.08%的用户
一次过，本来就是简单题。利用之前前序遍历的写法。很开心能有这个表现。
官方题解:
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        st1, st2 = [p], [q]
        # 结构不对就提前退出
        while st1 and st2:
            a, b = st1.pop(), st2.pop()
            if a and b and a.val == b.val:
                st1.append(a.right)
                st1.append(a.left)
                st2.append(b.right)
                st2.append(b.left)
            elif not a and not b:
                continue
            else:
                return False
        return True

root1, root2 = TreeNode(2), TreeNode(2,None,TreeNode(3))
print(Solution().isSameTree(root2, root2))
