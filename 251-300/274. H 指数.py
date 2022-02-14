'''
你的时间48ms,下面的用的是一样方法。但人家 20ms，击败100%提交。艺术代码。
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        index = 0
        citations.sort(reverse=True)
        for i in citations:
            if i > index:
                index +=1
        return index

官方题解第二种是用计数排序，好像也没排序，tc=O(n)，sc=O(n)实现的。
'''
from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for idx, i in enumerate(citations):
            h = n-idx
            if h <= i:
                return h

mt = [[3,0,6,1,5], ]
for i in mt:
    print(i, 'h ->', Solution().hIndex(i))

