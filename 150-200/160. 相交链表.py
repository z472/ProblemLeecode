'''
要求：满足 O(n) 时间复杂度，且仅用 O(1) 内存
执行用时：196 ms, 在所有 Python3 提交中击败了15.65%的用户
内存消耗：29.6 MB, 在所有 Python3 提交中击败了53.88%的用户
符合它进阶的这个要求。思路就是把链表数字的特征长度利用上。之前也有遇到过相似的。如142题

官方题解：符合进阶要求的是。双指针法。但是他的具体操作两个指针去遍历headA,headB。当一个到底部了。
就重定向到另一个链表的头结点去继续遍历。这样最后两个指针都走了  他们的长度之和 - 公共部分。也就是
相遇点为所求点。
下面是这种方法的较快的代码，tc击败了85%。但是用字典等存储空间的会更快。但不符合要求了。
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur1 = headA
        cur2 = headB
        while cur1!= cur2:
            cur1 = cur1.next if cur1 else headB
            cur2 = cur2.next if cur2 else headA
        return cur1
'''
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lena, lenb = 0, 0
        p1, p2 = headA, headB
        while p1 or p2:
            if p1:
                lena += 1
                p1 = p1.next
            if p2:
                lenb += 1
                p2 = p2.next
        if p1 != p2:
            return None
        p1, p2 = headA, headB
        while lena != lenb:
            if lena > lenb:
                p1 = p1.next
                lena -= 1
            else:
                p2 = p2.next
                lenb -= 1
        while p1 != p2:
            p1, p2 = p1.next, p2.next
        return p1

def onewayListNode(args: List):
    head = p = ListNode(args[0])
    for i in args:
        p.next = ListNode(i)
        p = p.next
    return (head, p)

mt = [1,3,5,8,23]
long = [0,3]
short = [-5,-3]
head = onewayListNode(mt)[0]
longhead, longtail = onewayListNode(long)
shorthead, shorttail = onewayListNode(short)
longtail.next = head
print(Solution().getIntersectionNode(longhead, shorthead) == head)


