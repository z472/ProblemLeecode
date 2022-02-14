'''
执行用时：92 ms, 在所有 Python3 提交中击败了54.00%的用户
内存消耗：21.6 MB, 在所有 Python3 提交中击败了44.18%的用户
一次过，也是第一个用类多方法解决的题。
官方题解：中序遍历二叉查找树的结果就是升序，然后他先存储起来。每次next和hasNext都为O(1)。
不过我的算法其实就是把中序遍历按具体操作拆分到next里。总的差别不大。
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def selectchildmin(self, p:TreeNode) -> None:
        # 修改self.stack
        while p:    # bug：p.left
            self.stack.append(p)
            p = p.left


    def __init__(self, root: TreeNode):
        self.stack = []
        self.selectchildmin(root)

    def next(self) -> int:
        wanttopop = self.stack.pop()
        if wanttopop.right:
            self.selectchildmin(wanttopop.right)     # bug
        # else:
        #     while self.stack and wanttopop.val > self.stack[-1].val:
        #         self.stack.pop()
        return wanttopop.val

    def hasNext(self) -> bool:
        return 0 if not self.stack else 1

childleft = TreeNode(3, None, TreeNode(5,TreeNode(4),TreeNode(6)))
childright = TreeNode(15, TreeNode(9), TreeNode(20))
root = TreeNode(7, childleft, childright)
mt = BSTIterator(root)
while mt.hasNext():
    print(mt.next(), end=' ')
    print('[', end='')
    for i in mt.stack:
        print(i.val, end=',')
    print(']')