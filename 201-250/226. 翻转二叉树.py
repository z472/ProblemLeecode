'''
执行用时：56 ms, 在所有 Python3 提交中击败了6.68%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了46.10%的用户
下面代码用时28ms，击败98.7%。凭什么？
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        def func(root):
            if root.left==None and root.right==None:
                return

            else:
                root.left,root.right =  root.right,root.left
                if root.left:
                    func(root.left)
                if root.right:
                    func(root.right)
        func(root)
        return root
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)
        return root


def output_values(root):
    sav, tag = [root], 0
    while True:
        x = []
        for i in sav:
            if i:
                print(i.val, end='\t')
                x.append(i.left if i.left else None)
                x.append(i.right if i.right else None)
            else:
                print('None', end='\t')

        print()
        sav = x
        if not [i for i in sav if i]:
            break


left = TreeNode(2, TreeNode(1), TreeNode(3))
right = TreeNode(7, None, TreeNode(9))
root = TreeNode(4, left, right)
output_values(root)
output_values(Solution().invertTree(root))
