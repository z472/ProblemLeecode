'''
执行用时：64 ms, 在所有 Python3 提交中击败了49.37%的用户
内存消耗：18.2 MB, 在所有 Python3 提交中击败了16.46%的用户
不会题目进阶的O(1)空间复杂度的解法。智商检测题。我败了。由于是成环，且路径是单向的。故它O(1)的解法为
快慢指针（龟兔赛跑）如果能成环，兔子会追上乌龟。否则兔子先到None。然后就注意几个边界条件。
下面是官方版本的提交。
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        tortoise = head
        rabbit = tortoise.next
        while rabbit and rabbit != tortoise:
            rabbit = rabbit.next if not rabbit.next else rabbit.next.next
            tortoise = tortoise.next
        if not rabbit:
            return False
        return True