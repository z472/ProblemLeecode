'''
执行用时：36 ms, 在所有 Python3 提交中击败了93.83%的用户
内存消耗：18.9 MB, 在所有 Python3 提交中击败了43.33%的用户
错了很多次，主要是逻辑有混乱。
'''
from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n == 1:
            return 0 if citations[0] < 1 else 1

        left, right = 0, n      # right 要设置成 n 为了后续判断
        while left < right:
            mid = (left+right)//2
            if citations[mid] == n-mid:
                return n-mid
            elif citations[mid] > n-mid:
                right = mid
            else:
                left = mid + 1

        return n-left

mt = [[0,1,3,5,6], [2,7,8,9,10], [0,1,2], [2], [2,4]]
bug = [[0], [0,0], [0,1]]
for i in mt+bug:
    print(Solution().hIndex(i))
