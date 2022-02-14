'''
执行用时：60 ms, 在所有 Python3 提交中击败了29.89%的用户
内存消耗：17.4 MB, 在所有 Python3 提交中击败了31.02%的用户
非正式解法，靠的中序遍历的输出列表是否是单调来判断。速度一般。
官方题解给出：递归和用非递归的中序遍历结果来看的两种，两种的tc和sc都为O(n)，但是如果是递归的话就不用走完，
走到半路就可以判断出来，应该好一些。
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
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
        print(res)
        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False
        return True


root1 = TreeNode(2, TreeNode(1), TreeNode(3))
root2 = TreeNode(5, None, TreeNode(7, TreeNode(6), TreeNode(9)))
root = TreeNode(4, root1, root2)
print(Solution().isValidBST(root))
