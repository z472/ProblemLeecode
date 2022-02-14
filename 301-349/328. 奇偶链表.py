'''
难度不大，好在写的快很简洁也没有bug，挺不错的。
'''
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pj, po = head, head.next
        p = po
        sav = head.next
        while p.next:
            if p == po:
                pj.next = p.next
                pj = pj.next
            else:
                po.next = p.next
                po = po.next
            p = p.next
        pj.next = sav
        po.next = None

        return head

mt = [1,2,3,4,5,6,7]
head = ListNode(mt[0])
p = head
for i in mt[1:]:
    p.next = ListNode(i)
    p = p.next
head = Solution().oddEvenList(head)
while head:
    print(head.val, end=' ')
    head = head.next
