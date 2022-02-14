'''
又是一个NP问题，不过最后用了一个DP来解决，也还ok，关键是理解它的思路，它dp设的内容和简单的递推表达式

'''
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        half = sum(nums)//2
        numslen = len(nums)
        def cd(idx, want)->bool:
            if idx == numslen:
                return False
            if nums[idx] == want or cd(idx+1, want-nums[idx]) or cd(idx+1, want):
                return True
            else:
                return False
        return cd(0, half)

mt = [[1,5,11,5], [1,2,3,5]]
for i in mt:
    print(i, '->>', Solution().canPartition(i))