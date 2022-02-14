'''
执行用时：40 ms, 在所有 Python3 提交中击败了75.79%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了17.83%的用户
很遗憾没能一次过，因为我多此一举的在else中写了一句p1, p2 = p1.next, p2.next，导致一个p2寻找的错误，这道题虽然看似代码
很丑陋，但是实际上是很标准的，先写普世规律，然后根据特殊情况，比如说越界、第一位的数等等。这里第一个数如果不是大于等于x的数的
前置就会是出错，于是给head前加上一个x-1的结点，然后p1从该位开始遍历。
官方题解：
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head, x):
        # head: ListNode, x: int) -> ListNode:
        # p1第一个大于等于x值的前面一位，保持不动；p2寻找p1后面的第一个小于x的值的前一位,p3保存一个结点
        p1 = ListNode(x - 1)
        p1.next = head
        p2 = p1
        head = p1
        while p2 and p1:
            if not p1.next or p1.next.val < x:
                p1 = p1.next
                p2 = p1
            elif not p2.next or p2.next.val >= x:  # 如果x比所有值都小，就走这条路走到底，巧合了
                # print(p2.val)
                p2 = p2.next
            else:
                p3 = p1.next
                p1.next = p2.next
                p2.next = p1.next.next  # 右侧写成p2.next.next貌似也可
                p1.next.next = p3
                # p1, p2 = p1.next, p2.next
        return head.next


head = p = ListNode(1)
mt = [[-1, 0, 1, 4, 3, 2, 5, 2], [2, 1], [1, 4, 3, 0, 2, 5, 2]]
for i in mt[2]:
    p.next = ListNode(i)
    p = p.next
a = Solution()
p = head
while head.next:
    print(head.next.val, end='')
    head = head.next
x = 3
print('  x=', x)
head = a.partition(p.next, x)
while head:
    print(head.val, end='')
    head = head.next
