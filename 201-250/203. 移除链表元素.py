'''
执行用时：64 ms, 在所有 Python3 提交中击败了91.09%的用户
内存消耗：17.8 MB, 在所有 Python3 提交中击败了82.74%的用户
心疼我编码的时间。这么简单的小问题，真的是bug黑洞。过程黑洞。边界值黑洞。
官方题解：
what。哨兵写法（伪头）   关键还是核心循环写法的不同。我是选一个正确的连接给prev结点的next.
官方更好的写法就是不选择，但是如果连错了可以被后续操作给修改好。最优雅的地方就是它的写法覆盖了
许多的边界条件。包括最后如果最后一个值为val时，都被它的过程“轻描淡写”地覆盖掉了。

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head

        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return sentinel.next
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre = headpre = ListNode(0, head)
        last = pre.next
        # last 不断寻找pre后合法值结点
        while last:
            if last.val != val:
                pre.next = last     # 两条路
            else:
                last = last.next
                continue
            last = last.next
            if last:    # bug逻辑写反了。和官方一比这里不写更好。
                pre = pre.next

        if headpre.next and headpre.next.val == val:
            return None

        if pre.next and pre.next.val == val:
            pre.next = None
        return headpre.next

mt = [1,2,1,4,3,2,1]
bug = [7,7,7,7]
def makeListNode(mt:list):
    p = head = ListNode(mt[0])
    for i in mt[1:]:
        p.next = ListNode(i)
        p = p.next
    return head

def printListNode(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()

printListNode(Solution().removeElements(makeListNode(mt), 2))
printListNode(Solution().removeElements(makeListNode(mt), 1))
print(None == printListNode(Solution().removeElements(makeListNode(bug), 7)))
print(None == printListNode(Solution().removeElements(None, 7)))
printListNode(Solution().removeElements(makeListNode(bug), 0))
