'''
执行用时：64 ms, 在所有 Python3 提交中击败了42.34%的用户
内存消耗：17.8 MB, 在所有 Python3 提交中击败了59.89%的用户
官方题解的SC为O(1)思路不会，这是看后练习编码。但是错在了[1,2]然后2甩到1的环这个测试用例两次。
遗憾的是官方O(1)版本没有Py3的，下面是一个较好的同思路的代码。sc仅比我多30kb，鉴于全部占用为1.8万kb。
可视为一样。它的tc=56ms，已击败82%。比我速度快了12.5%。就是循环条件完全放空，减少掉了一些if判断。

官方题解：O(1)。同141为快慢指针。但它多了简单的数学推导。推导的式子 未知数 很多，会感觉是个无用品。
但是具体算法的执行还是靠对推导式的理解和当前已知信息。方法难以归类，算是很吃理解的一个题。
class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return
            fast, slow = fast.next.next, slow.next
            if fast == slow: break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        tortoise = rabbit = head
        while rabbit != tortoise or (tortoise == head and rabbit == head):
            if not rabbit or not rabbit.next:
                return None
            rabbit = rabbit.next.next
            tortoise = tortoise.next
            if rabbit == head:
                break

        pre = head
        while pre != rabbit:
            pre, rabbit = pre.next, rabbit.next

        return pre.val


mt = [1, 2, 3, 4, 5, 6, 7]
p = head = ListNode(1)
for i in range(len(mt) - 1):
    p.next = ListNode(mt[i + 1])
    p = p.next
print(p.next)
p.next = head.next.next  # 环在3那里为接入点

head = ListNode(1)
head.next = ListNode(2)
head.next.next = head
p = head
for i in range(5):
    print(p.val, end=' ')
    p = p.next
print()
print(Solution().detectCycle(head))
