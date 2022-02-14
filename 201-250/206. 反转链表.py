'''
执行用时：44 ms, 在所有 Python3 提交中击败了63.17%的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了48.23%的用户
依旧是一个没啥成就感的题。
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        ptail, phead = head.next, head
        phead.next = None
        while ptail:
            sav = ptail.next
            ptail.next = phead
            phead = ptail
            ptail = sav
        return phead

def make(list):
    head = p = ListNode(list[0])
    for i in list[1:]:
        p.next = ListNode(i)
        p = p.next
    return head

def show(head:ListNode):
    while head:
        print(head.val,end=' ')
        head = head.next
    print()

mt = [1,2,3,4,5]
show(Solution().reverseList(make(mt)))