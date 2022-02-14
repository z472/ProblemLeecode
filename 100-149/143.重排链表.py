'''
官方题解方法二：寻找链表中点 + 右半段链表逆序 + 合并链表。
它总能整出点新花样。
实际编码练习。
执行用时：96 ms, 在所有 Python3 提交中击败了69.16%的用户
内存消耗：22.8 MB, 在所有 Python3 提交中击败了93.59%的用户
没有它官方题解里的三步走，估计还要摸索很久。我这是根据它三步骤下面的一行提示。每个步骤的实现都要动下脑筋。
还有就是奇偶数的区别和next指针是否归到None。  我的代码的问题，多个变量导致步骤变得更清晰，但是容易忽视掉部分变量的更新，维护。

下面是官方题解的py3代码：
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)

    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev

    def mergeList(self, l1: ListNode, l2: ListNode):
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next

            l1.next = l2
            l1 = l1_tmp

            l2.next = l1
            l2 = l2_tmp
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        fast, slow = head, head
        while True:
            if not fast or not fast.next:
                break
            slow, fast = slow.next, fast.next.next
        mid = slow
        movetofront = mid.next
        front = mid
        while movetofront:
            mid.next = movetofront.next
            movetofront.next = front
            front = movetofront
            movetofront = mid.next
        # mid.next什么时候改为None了
        # mid.next = None
        p = head
        while p != mid:
            savleft, savright = p.next, front.next

            p.next = front
            front.next = savleft  # bug
            front = savright
            p = savleft
        mid.next = None
        return head


p = head = ListNode(1)
for i in range(2, 4):
    p.next = ListNode(i)
    p = p.next
head = Solution().reorderList(head)
while head:
    print(head.val, end=' ')
    head = head.next
