'''
执行用时：44 ms, 在所有 Python3 提交中击败了82.99%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了17.36%的用户
不是一次过，难受。忘了head为空的情况。没什么好说的。
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        # head: ListNode) -> ListNode:
        if not head:    # 第一次没写这里，错了，ohno难受
            return None
        p1 = head
        p2 = p1.next
        while p2:
            if p1.val != p2.val:
                if p1.next == p2:
                    p1 = p1.next
                else:
                    p1.next = p2
                    p1 = p1.next
            p2 = p2.next
        p1.next = None
        return head

mt = [1,2,2,3,4,4,4]
head = p = ListNode(mt[0])
for i in mt[1:]:
    p.next = ListNode(i)
    p = p.next
a = Solution()
head = a.deleteDuplicates(head)
while head:
    print(head.val, end=' ')
    head = head.next