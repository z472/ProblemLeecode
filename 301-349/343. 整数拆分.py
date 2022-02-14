'''
执行用时：44 ms, 在所有 Python3 提交中击败了57.49%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了30.35%的用户
自己分析出的dp一次过。

该题还可以优化dp。让tc = O(N)。甚至是数学方法 tc = O(1).

good！今天提交成功的第四个中等题，还简单分析看了两个困难题。
'''
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1
        dp = [1]*(n+1)
        for i in range(2, n+1):
            maxi = i
            for j in range(1, i//2+1):
                maxi = max(maxi, dp[i-j]*dp[j])
            dp[i] = maxi
        print(dp)
        return dp[-1]

mt = [10,]
for i in mt:
    print(i, '-> ', Solution().integerBreak(i))