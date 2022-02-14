'''
此题官方有多种方法。其中前几种都是平常的思路。Boyer-Moore 算法是较为新奇的东西。也比较难理解。
'''
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
