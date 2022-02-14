from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curmin = prices[0]
        profitmax = 0
        for i in prices:
            if i < curmin:
                curmin = i
                continue
            else:
                profitmax = max(i-curmin, profitmax)
        return profitmax

mt = [[7,1,5,3,6,4],[7,6,4,3,1]]
for i in mt:
    print(i, Solution().maxProfit(i))