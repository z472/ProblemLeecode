'''
执行用时：68 ms, 在所有 Python3 提交中击败了12.19%的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了21.15%的用户
构思墨迹，写的时候又有收尾位置的bug，表现也一般。难受了呀。

同样思路 32ms代码。就是具体操作上，我是判断多了，我是让程序到特定位置然后加运算一下。
它是把我加运算分多步做了。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = point = 0
        for i in range(len(prices)):
            if prices[i] - prices[point] <= 0:
                point = i
            else:
                sum += prices[i] - prices[point]
                point = i
        return sum
28ms的代码，pythonic
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tmp = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit = prices[i] - prices[i-1]
                tmp += profit
        return tmp
'''
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 有无利润的起始值，0是没有，1是有了
        tag = 0
        ret = 0
        lenpri = len(prices)
        curmin = prices[0]
        for i in range(1, lenpri):
            if tag == 0 and prices[i-1] < prices[i]:
                tag = 1
                curmin = prices[i-1]
            elif prices[i-1] > prices[i]:
                ret += prices[i-1] - curmin
                curmin = prices[i]
                tag = 0

        return ret + prices[-1] - curmin

mt = [[7,1,5,3,6,4], [1,2,3,4,5], [2], [1,4], [4,2]]
for i in mt:
    print(i, Solution().maxProfit(i))

