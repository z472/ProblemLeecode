'''
要求:tc = O(logN)
执行用时：40 ms, 在所有 Python3 提交中击败了59.80%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了89.43%的用户
思路
'''
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left

mt = [[3,2,1], [1,2,3], [1,3,2]]
for i in mt:
    print('in:', i)
    print(Solution().findPeakElement(i))