from typing import List

'''
自己没有分析正确，下面是网友DP思路的实现。也是官方题解的方法。tc击败98.9%。比最下面的要快25%
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp_min = min(0, nums[0])
        dp_max = max(0, nums[0])
        max_values = dp_max
        for n in nums[1:]:
            if n >= 0:
                dp_max = max([n * dp_max, n])
                dp_min = dp_min * n 
            else:
                tmp = dp_max
                dp_max = dp_min * n 
                dp_min = min([n * tmp, n])
            max_values = max([max_values, dp_max])
        return max_values
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res


mt = [[2, 3, -2, 4, 8, 0, 20, 4], [-2, 0, -1], [1, -10], ]
for i in mt:
    print('in:', i)
    print(Solution().maxProduct(i))
