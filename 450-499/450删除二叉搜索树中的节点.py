class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        p = root
        while p.val != key:
            if p.val < key:
                p = p.right
            else:
                p = p.left
        # key节点的位置不变，但里面的值替换为它右边分支的最小值；若没有右边分支则原地删除该节点
        if p.right:
            while True:
                pass
        # 稍微想象一下编码细节，就明白为何这题也算是“中等”了，完全是折磨人的编码细节题。
