'''
当你看到dp这个word[i]!=word[j]的写法，再看看dp代表的含义。和我设置完全
一样，真想给自己一个大巴掌。dp近在咫尺，遗憾似海深。我对wi != wj 想的是wi
和wd[i-1]wd[j-x]这些值能否+1,完全没有考虑和“周围元素”的关系，想一下这些
元素可以提示到自己，这是很大的失误，你在干拔这个逻辑。

这题从根本上有个需要论证的点，当前最长公共序列和全局最长公共序列是连续的吗？
换问法：当前最长公共序列不取这个字符，但是全局最长的后面有取到它？

这题目让我想了很多，主要在题目的做法上，如何dfs,如何贪心，不知道怎样去到了dp上。
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        lcs = dp[m][n]
        return m - lcs + n - lcs


