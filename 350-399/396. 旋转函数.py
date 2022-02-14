'''
执行用时：64 ms, 在所有 Python3 提交中击败了73.91%的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了91.93%的用户

30分钟解决的中等题。秒出思路。
没有bug。唯一问题是边听歌边写，有点写不出来，老是溜号。
看了下44ms的提交代码，和我的差不多。
'''
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        nexclude = sum(nums, -nums[-1])
        partialsum = 0
        for idx, i in enumerate(nums):
            partialsum += idx * i
        maxret = partialsum
        n = len(nums)
        for i in range(1, n):
            partialsum += nexclude - (n - 1) * nums[n - i]
            maxret = max(maxret, partialsum)
            nexclude += nums[n - i] - nums[n - i - 1]
        return maxret


mt = [[4, 3, 2, 6], ]
for i in mt:
    print(i, Solution().maxRotateFunction(i))
