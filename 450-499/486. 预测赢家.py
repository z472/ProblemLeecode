'''
这题的dp解法很优美，详见：
https://leetcode-cn.com/problems/predict-the-winner/solution/yu-ce-ying-jia-by-leetcode-solution/

从设二维数组，表达抽象，到推dp表达式，都十分优秀。既有 从已知到未知推导dp表达式，一步步前进的整个流程的逻辑性。还有建模这个创建
抽象的跳跃性。小而丰富。
'''
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [[0 for j in range(len(nums))] for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    dp[i][i] = nums[i]
        for time in range(len(nums) - 1,0,-1):
            for x in range(time):
                i,j = x, (len(nums)-time)+x
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][-1] >= 0

test = [[1,5,233,7],]
for i in test:
    print(Solution().PredictTheWinner(i))
