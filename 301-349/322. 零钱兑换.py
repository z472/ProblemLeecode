'''
执行用时：1628 ms, 在所有 Python3 提交中击败了24.25%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了27.65%的用户

算法构思：自己没想出来什么好的办法。知道它是完全背包问题。之前也做过一个该问题279.完全平方数的题。但它们
的分析还是很不相同的。那道题是设置 遍历深度的广度优先遍历，用该方法的来减少递归下去的时间，那个会提前返回。
    跑题了。这个题的分析它使用的类似最最基础的DP方法---斐波那契数列dp问题，注意只是有点像。
    tc = O(S*n) S 就是最大的数值。它的递推式其实比较难以理解正确性的点是，它为何不会漏解？？？
    我的感觉就是它 + 1操作配合前面min从i=coins[0]到coins[-1]。相当于是遍历了所有可能。所以不会漏解。
反思：这是一道看似复杂，但是很基础的dp题。我分析时主要想的是贪心，还有如果输出-1，现在看来都是很边缘化的思考。
没抓住问题本质。这种dp可以说是最最基础的了。我做了这么多居然还不会。。。QAQ

编码体验：写的时候感觉很方便由于是用的字典来存储。就是那个dict.get()出来的值是0然后让if判断成了错误。
'''
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dpamoutdict = {0: 0}
        for pay in range(amount+1):
            curmin = amount + 1
            for i in coins:
                if dpamoutdict.get(pay - i, -1) != -1:    # dict.get出来的值可能是0.它不是有值就为正确.bug
                    curmin = min(curmin, dpamoutdict[pay - i])
            if curmin != amount + 1:
                dpamoutdict[pay] = curmin + 1
        # print(dpamoutdict)
        if dpamoutdict.get(amount, -1) != -1:   # 否则你的 0 -》 0的输出就为-1了
            return dpamoutdict[amount]
        return -1

mt = [([1,2,5], 11), ([2], 3), ([1], 2), ]
for i in mt[:]:
    print(i, '->', Solution().coinChange(i[0], i[1]))