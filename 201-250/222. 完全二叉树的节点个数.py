'''
执行用时：76 ms, 在所有 Python3 提交中击败了94.18%的用户
内存消耗：21.7 MB, 在所有 Python3 提交中击败了31.00%的用户
思路来自官方题解，本题是搜索完全二叉树的个数，tc要小于O(n)。需要创新方法。
官方题解：由于完全二叉树除了最后一层，其他都是2的（0，1,2...）幂。每一层的数量等于二进数的第h位（从右向左看的话）
就是这样一个奇妙的联系。数--形的一个美妙结合。又由于完全二叉树的特性，可以一直左遍历获得树的高度。然后就是二分来求。
后面二分还是有点难写，如果不是预处理一下，条件还是很杂乱的。想了一会。
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        h = -1
        if not root:
            return 0
        p = root
        while p:
            h += 1
            p = p.left
        minimum = 2 ** h
        maximum = 2 ** (h+1)    # 最后一行最大值为2^(n+1)-1，但是那样不好写二分法，这里很帅的
        while minimum + 1 < maximum:
            mid = (minimum + maximum) // 2
            str = bin(mid)[3:]
            p = root
            for i in str:
                if i == '1':
                    p = p.right
                else:
                    p = p.left
            if p:
                minimum = mid
            else:
                maximum = mid

        return minimum


left = TreeNode(2,)
right = TreeNode(3,  )
root = TreeNode(1,)
print(Solution().countNodes(root))
