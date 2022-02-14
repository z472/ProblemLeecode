'''
执行用时：224 ms, 在所有 Python3 提交中击败了53.83%的用户
内存消耗：20.9 MB, 在所有 Python3 提交中击败了42.57%的用户

一次过，还是不错的。
这题目和之前某几个题很相似，目前的用3个变量的dp其实是从dp一维数组逐渐优化后的模样。
这题很容易晕，逻辑就现在即使是一次过，做的很好，但仍不能说(shuo)服我自己。我推导时候
想的是，这是两种状态，遍历到当前值只需要考虑前面的状态。
'''
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        b, s = -prices[0], 0
        for i in range(len(prices)):
            # b=dp[i][0] 当前买入的最大收益，s=dp[i][1] 当前卖出的最大收益
            # b= max(dp[i-1][1]-pi, dp[i-1][0]),s = max(pi-fee+dp[i-1][0], dp[i-1][1])
            pres = s
            s = max(prices[i]-fee+b, s)
            b = max(pres-prices[i], b)
        return s

test = [([1,3,2,8,4,9], 2), ([1,3,7,5,10,3], 3)]
for i in test:
    print(Solution().maxProfit(i[0],i[1]))