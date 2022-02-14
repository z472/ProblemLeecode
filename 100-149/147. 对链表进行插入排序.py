'''
执行用时：168 ms, 在所有 Python3 提交中击败了88.80%的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了73.85%的用户
一次过，运行表现还可以。出了一个bug。是我的链表没有链接好。纵观整个解题过程从形成思路到编码实现，首先是效率不错，
很多条件细节用了形象的savhead,savtail这样的名字来表示，增速不少。     但还有一些"场外"因素我觉得也是很重要。
早上很快的起床，没有沉迷手机的信息里。吃完早点，冲浪适可而止。做题的话，没有听歌，这也是提速不少。让编码的临场反应
变快了些。   主要就是管理好自己的心态，别胡思乱想来干扰你。
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        savhead = savtail = t = head
        waitinsert = head.next
        while waitinsert:
            savnode = waitinsert.next
            waitinsert.next = savhead
            if waitinsert.val < savtail.val:
                t = waitinsert
                while waitinsert.val > t.next.val:
                    t = t.next
                waitinsert.next = t.next
                if t != waitinsert:
                    t.next = waitinsert
                else:
                    savhead = waitinsert
            else:
                savtail.next = waitinsert
                savtail = waitinsert
            waitinsert = savnode
        savtail.next = None
        return savhead

mt = [3,4,1,5,2]    # ,5,2
p = head = ListNode(3)
for i in mt[1:]:
    p.next = ListNode(i)
    p = p.next
head = Solution().insertionSortList(head)
while head:
    print(head.val, end=' ')
    head = head.next



