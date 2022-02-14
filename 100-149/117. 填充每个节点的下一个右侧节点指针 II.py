'''
执行用时：52 ms, 在所有 Python3 提交中击败了92.95%的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了27.49%的用户
一次过，没啥好说的，算法和前一个题几乎一致，就是特殊情况更多了，偏移的修改情况增多。感觉代码写的很慢，因为想写的不太啰嗦。
关键的变量有点多了，chl,chlnext,fat,beg一共有四个，而你的整个循环做一遍下来才改变一个结点位置，应该把同一行的偏移量修改
放在一个小的while中。看下别人的代码，递归写的速度会稍慢，但空间会达到14MB。这题主要是细心，和练手。
'''
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        beg, fat, chl = root, root, root
        if not root or (not root.left and not root.right):
            return root

        beg = chl = root.left if root.left else root.right
        # 多条if判断，增加了出错概率也增加了可读性，但是有些逻辑是必须要表达的，别怕写的啰嗦，都可以改好的
        while chl:
            chlnext = chl
            while chlnext == chl and fat:      # 不断向右走,找到孩子的右侧结点
                # 正反面到底是要写一个的，挑选代码少的去写，用空白来表意
                if fat.left and fat.left != chl:
                    chlnext = fat.left
                elif fat.right and fat.right != chl:
                    chlnext = fat.right
                if chlnext == chl:
                    fat = fat.next      # bug1
            # 处理好偏移量fat,chl
            if fat:     # 找到了chl右侧结点
                chl.next = chlnext
                chl = chl.next
                if fat.right and fat.right == chl:
                    fat = fat.next
            else:       # 找不到chl的右侧的结点
                fat = beg
                while fat and not fat.left and not fat.right:
                    fat = fat.next
                if not fat:
                    break
                else:
                    chl = fat.left if fat.left else fat.right
                beg = chl

        return root

def printNode(root):
    beg = root
    res = []
    while True:
        while beg and not beg.left and not beg.right:
            beg = beg.next
        if not beg:
            break
        p = beg.left if beg.left else beg.right
        beg = p
        while p:
            res.append(p.val)
            if not p.next:
                res.append('#')
            p = p.next

    return res



rl, rr = Node(2, Node(4), Node(5)), Node(3, None, Node(6))
root = Node(1, rl, None)
print(printNode(Solution().connect(root)))




