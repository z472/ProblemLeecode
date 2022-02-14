from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def getright(root):
            if root.left:
                node = root.left
                while node.right:
                    node = node.right
                node.ret = root
        res = []
        def dfs(root):
            if root.left:
                getright(root)
                ret = dfs(root.left)
                if ret != root:
                    return ret
                else:
                    res.append(root.val)

            if root.right:
                if not root.left:
                    res.append(root.val)
                dfs(root.right)
            if not root.left and not root.right:
                res.append(root.val)

            if getattr(root, 'ret', None):
                # res.append(root.val)
                return root.ret

        dfs(root)
        return res

left = TreeNode(1,TreeNode(-1), TreeNode(3,TreeNode(2)))
right = TreeNode(5,None,TreeNode(5,None,TreeNode(9,TreeNode(6))))
test = TreeNode(4,left,right)
test1 = TreeNode(2,TreeNode(1))
print(Solution().findMode(test))
