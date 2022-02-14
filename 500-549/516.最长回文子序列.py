'''
执行用时：280 ms, 在所有 Python3 提交中击败了99.85%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了97.69%的用户

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n <= 1 or s == s[::-1]:
           return n
        dp = [0] * n
        for i in range(n):
            dp[i] = 1
            prev = 0
            for j in range(i - 1, -1, -1):
                dpj = dp[j]
                if s[i] == s[j]:
                    prev, dp[j] = dpj, prev + 2
                else:
                    prev = dpj
                    if dpj < dp[j+1]:
                        dp[j] = dp[j+1]
        return dp[0]
'''
# 你 的 代 码 ~
# 执行用时：2300 ms, 在所有 Python3 提交中击败了8.52%的用户
# 内存消耗：31.9 MB, 在所有 Python3 提交中击败了15.84%的用户
from typing import List


class Solution:
    def longestPalindromeSubseq(self, s: str) -> List:
        dp = [[1 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(1, len(s)):
            x, y = 0, i
            for j in range(len(s) - i):
                if s[x] == s[y]:
                    if y - x == 1:
                        dp[x][y] = 2
                    elif y > 0 and x < len(s) - 1:
                        dp[x][y] = dp[x + 1][y - 1] + 2
                else:
                    if y > 0:
                        dp[x][y] = dp[x][y - 1]
                    if x < len(s) - 1:
                        dp[x][y] = max(dp[x][y], dp[x + 1][y])
                x, y = x+1, y+1
        return dp

test = ['bbbab', 'cbbd',]
for i in test[:]:
    print('in:', i)
    t = Solution().longestPalindromeSubseq(i)
    for _ in t:
        print(_)