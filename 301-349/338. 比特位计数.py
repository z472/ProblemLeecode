'''
执行用时：52 ms, 在所有 Python3 提交中击败了96.22%的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了97.97%的用户
一次过，分析花了点时间。
'''
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]*(num+1)
        nn = None
        for i in range(1, num+1):
            if i & (i-1) == 0:
                dp[i] = 1
                nn = i
            else:
                dp[i] = dp[i%nn] + 1
        return dp

mt = [16]
for i in mt:
    print(i, '->', Solution().countBits(i))
