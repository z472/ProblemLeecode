'''
不确定长度的随机数问题---蓄水池算法。

每次以1/i(i为当前长度）的概率来把当前值作为输出。i是每次遇到一个新值就加一。
https://leetcode-cn.com/problems/linked-list-random-node/solution/monkti-jie-yong-zui-shao-de-yu-yan-he-da-zno0/
'''
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """



    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """