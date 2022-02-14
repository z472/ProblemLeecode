'''
执行用时：64 ms, 在所有 Python3 提交中击败了94.77%的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了51.54%的用户

一次过，但是我觉得编码太慢了，没难度的东西，bug无限循环了两次，是因为忘了偏移往下走。
还有就是各种类型处理的bug，让列表获取.val，种种问题。

思路就是最好的，不用递归，用已经建好的next，官方题解最后一个。但它的编码时按照楼层写的，看上去是循环嵌套，但是实际上
仍是O(n)。我的是一个循环，但是每次偏移写的多了一点。
'''
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        fat, chl = root, None
        if fat and fat.left:
            chl = root.left
        else:
            return fat
        beg = chl
        while beg:
            if fat.left == chl:
                chl.next = fat.right
                chl = chl.next
            elif fat.next:
                chl.next = fat.next.left
                chl, fat = chl.next, fat.next
            else:
                fat, chl = beg, beg.left
                beg = beg.left

        return root


def printNode(root: Node) -> None:
    beg = [i for i in [root] if i]
    res = [beg + ['#'], ]
    while beg != ['#']:
        sav, i = [], beg[0]
        while i:
            if i.left:
                sav.append(i.left)
                sav.append(i.right)
            if i.next:
                i = i.next
            else:
                sav.append('#')
                break
        res.append(sav)
        beg = sav
    return res


rl = Node(2, Node(4), Node(5))
rr = Node(3, Node(6), Node(7))
root = Node(1, rl, rr)
for i in printNode(Solution().connect(root)):
    for j in i[:-1]:
        print(j.val, end=' ')
    if i[-1] == '#':
        print('#')
