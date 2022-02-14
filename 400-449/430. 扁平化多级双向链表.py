'''
执行用时：36 ms, 在所有 Python3 提交中击败了92.59%的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了5.25%的用户

210805 No.1
一次过，递归，双向链表，改写数据结构。
'''
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        cur = Node(head.val)
        if head.child:
            cur.next = self.flatten(head.child)
            cur.next.prev = cur
        if head.next:
            p = cur
            while p.next:
                p = p.next
            p.next = self.flatten(head.next)
            p.next.prev = p
        return cur