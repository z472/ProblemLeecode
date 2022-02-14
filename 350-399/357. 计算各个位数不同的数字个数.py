'''
执行用时：36 ms, 在所有 Python3 提交中击败了82.52%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了65.96%的用户

居然是一个中等题。
'''
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [9]*11 if n > 10 else [9]*(n+1)
        for i in range(2, n+1):
            if i > 10:
                break
            dp[i] = dp[i-1]*(11-i)
        print(dp)
        return sum(dp)-8

mt = [0,4,11,100, 2]
for i in mt:
    print(i, Solution().countNumbersWithUniqueDigits(i))