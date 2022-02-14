'''
执行用时：40 ms, 在所有 Python3 提交中击败了81.78%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了32.97%的用户
    这题主要是在链表上弄，没啥需要动脑的东西，主要是测试这个算法
还要构造链表出来，出现了两次的变量指到了NoneType，却以为该变量
是个ListNode()的情况，需要注意。
    没有一次过，主要是没写head输入为None的情况。算是自己恶心自
己了，因为测试的时候还说要注意这点。但被出现的bug转移注意力了。有
点可惜。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k):
        # head: ListNode, k: int) -> ListNode:
        if not head:
            return
        le = 1
        p2 = head
        while p2.next:
            le += 1
            p2 = p2.next
        k = k % le
        p2.next = head
        for _ in range(le-k-1):
            head = head.next
        p2 = head.next
        head.next = None
        return p2
mytest = [3,2,1,0]
a = Solution()
head = p = ListNode(val=3)
for i in mytest[1:]:
    p.next = ListNode(i)
    p = p.next
p = head
inp, k = [], 5
while p:
    inp.append(p.val)
    p = p.next
print('in:', inp, 'k=', k)
newhead = a.rotateRight(head, k)
out = []
while newhead:
    out.append(newhead.val)
    newhead = newhead.next
print('out:', out)