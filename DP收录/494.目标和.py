'''
背包问题的变形，独立自主解决的。
'''
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[i][cursum] = [yes, no] yes表示加当前的Nums[i]值为cursum的
        # 个数，no是不加当前值且值为cursum的个数
        # dp[i][cursum](no) = dp[i-1][cursum][yes]+dp[i-1][cursum][no]
        # dp[i][cursum][yes] = dp[i][cursum-nums[i]][no]
        # 最后res = sum(dp[-1][target])
        if abs(target) > sum(nums) or (target + sum(nums)) % 2:
            return 0
        target = (target + sum(nums))//2
        dp = [[[0,0] for _ in range(target+1)] for i in range(len(nums))]
        if nums[0] < target+1:
            dp[0][nums[0]][0] = 1
        # 真的有点搞，下面这个逻辑
        dp[0][0][1] = 1
        for i in range(1, len(nums)):
            for j in range(target+1):
                dp[i][j][1] = dp[i-1][j][0] + dp[i-1][j][1]
                if j >= nums[i]:
                    dp[i][j][0] = dp[i][j-nums[i]][1]
        return sum(dp[-1][target])