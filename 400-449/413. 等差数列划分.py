'''
执行用时：40 ms, 在所有 Python3 提交中击败了69.97%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了17.75%的用户
时间复杂度O(n),空间O(1)。并不是很难，思路秒出。提交一次过。
'''

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        numslen = len(nums)
        if numslen < 3:
            return 0
        stepsize = nums[1] - nums[0]
        ilen = 2
        res = 0
        for idx in range(2, numslen):
            if nums[idx] - nums[idx - 1] != stepsize:
                if ilen >= 3:
                    res += (ilen - 1) * (ilen - 2) // 2
                ilen = 2
                stepsize = nums[idx] - nums[idx - 1]
            else:
                ilen += 1
        if ilen >= 3:
            res += (ilen - 1) * (ilen - 2) // 2
        return res


mt = [[1, 3, 5, 7, 9, 3, -1, -5, -9], [7, 7, 7, 7, 7, ]]
for i in mt:
    print(i, '->>', Solution().numberOfArithmeticSlices(i))
