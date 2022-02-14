'''
执行用时：36 ms, 在所有 Python3 提交中击败了82.55%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了26.39%的用户
实在想不出来怎么一次遍历就能修改的方法，就看了官方题解，用递归来实现，很轻松的思路，用指针指向left，递归到right的位置，
然后就是回溯，每个回溯中都交换值，并且p_left = p_left.next。由于是递归的嘛，回溯的话可以自动得到right前置的指针。
但我写的时候，居然是导致回溯到虚空之中了。忙活了一段时间。   感觉是思考的时间不够，并且写的极短代码居然漏洞百出。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left, right):
        # head: ListNode, left: int, right: int) -> ListNode:
        global tag, p1
        p1, tag = head, 0
        if right == 1:
            return head
        for _ in range(left - 1):
            p1 = p1.next

        # print('this ', p1.val)
        def child(x, p2):
            global tag, p1
            if x == right:
                tag = 1
            if tag == 0 and x != right:
                child(x + 1, p2.next)
            if x > (right + left) // 2:
                # print(x, ' ', p1.val, ' ', p2.val)
                p1.val, p2.val = p2.val, p1.val
                p1 = p1.next
                # print(p1.val)

        child(left, p1)
        return head


head = ListNode(1)
p = head
for _ in range(2, 7):
    p.next = ListNode(_)
    p = p.next
head = Solution().reverseBetween(head, 1, 2)
while head:
    print(head.val, end='')
    head = head.next
