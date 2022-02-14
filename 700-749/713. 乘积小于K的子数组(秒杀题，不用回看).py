'''
执行用时：120 ms, 在所有 Python3 提交中击败了99.31%的用户
内存消耗：17.2 MB, 在所有 Python3 提交中击败了5.08%的用户

双指针，纯练手题，看下官方代码（和我写的居然一模一样），我代码也修改了一次，不断简化
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans

'''
from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l  = 0
        cur = 1
        res = 0
        if k <= 1:
            return 0
        for i in range(len(nums)):
            cur *= nums[i]
            while cur >= k:
                cur //= nums[l]
                l += 1
            res += i - l + 1
        return res

test = [([10,5,2,6], 100)]
for i in test:
    print(Solution().numSubarrayProductLessThanK(i[0],i[1]))