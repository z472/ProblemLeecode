'''
贪心，没什么好说的，代码也是和官方py3很相似。
'''
from typing import List
from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d1 = Counter(answers)
        res = 0
        for a,na in d1.items():
            res += (a+1)*(((na-1)//(a+1))+1)
        return res