'''

题不是很难，分析的拉跨，可惜。下面的算法错的。
'''
from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0

        def get1(i):
            nonlocal res
            t = bin(i).count('1')
            res += t
            return t

        for i in range(len(nums), 0, -1):
            for j in range(i - 1):
                get1(nums[j] ^ nums[j + 1])
                nums[j] = nums[j] ^ nums[j + 1]
        return res


test = [[4, 14, 2], ]
wrong = [ [4,14,4],  [4,14,4,14]]
for i in wrong[-1:]:
    print(Solution().totalHammingDistance(i))