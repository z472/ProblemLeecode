'''
修改前：
执行用时：56 ms, 在所有 Python3 提交中击败了17.79%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了16.66%的用户
修改后：
执行用时：48 ms, 在所有 Python3 提交中击败了63.59%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了30.00%的用户
第二次过的，而且表现很差，代码我觉得是特别糟糕，在本上写的很多，最后决定加入一个sav保存前置的值。p1最初为None，p2是遍历的，用一个
核心判断来遍历得到该位置是否唯一，唯一就给p1，否就给sav。由于我这个判断写的有浪费的地方。就把条件拆开来改了一下，第二个版本终于看起
来还过的去的。 自己测试的时候没有把p1的next改成None。导致迷惑了一阵：怎么输出了这么多？很搞笑。

官方题解：
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        # head: ListNode) -> ListNode:
        if not head:
            return None
        p1, p2, sav = None, head, head.val-1
        while p2.next:  # 只有一个值进不去，下面的if在通过之后修改了一遍，执行的浪费减少了
            if p2.val != sav:   # 前置判断是否唯一
                if p2.val != p2.next.val:   # 后置判断
                    if not p1:
                        p1 = p2
                        head = p1
                    else:
                        p1.next = p2
                        p1 = p1.next
                else:
                    sav = p2.val
            p2 = p2.next
        if p1:
            if sav != p2.val:
                p1.next = p2
                p1 = p1.next
            p1.next = None
        elif sav != p2.val:
            head = p2
        else:
            head = None
        return head

mt = [1,2,3,4,4,4,5]  # 1,1,2,3,4,4,4,5
head = p = ListNode(mt[0])
for i in mt[1:]:
    p.next = ListNode(i)
    p = p.next
a = Solution()
head = a.deleteDuplicates(head)
print(head == None)
while head:
    print(head.val, end=' ')
    head = head.next