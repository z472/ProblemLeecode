'''
分析了一会，决定用dp解决。我设置的dp[i][j]是从s1[0:i]和s2[0:j]开始保存的最大公共字符串的ascii和，
当然还有前两个元素。那两个数据就是dp推导出现错误的原因，但最深处的原因还是对于数据的理解有偏差，用法有些
问题。我最初想保存的是公共字符串，想先间接点dp，最后转化为ascii和。但我的dp推导方式出错，被我设置的前两个
数据所困，不继续写主要是因为当出现同样ascii和时我前两个元素没有何时的dp策略。

这题主要还是差在dp推导式上，对s1[:i]和s2[:j]都非空的情况的推导，下面错误代码就是理解我最初思路用的。
这题的官方题解，看了几乎是秒懂，它设的dp形式是一样的，但是dp内容就是减少的ascii和。和我的dp几乎全部是
反过来的，但是内容是一样的。很可惜。对数据的理解能力决定了你对数据的操作。

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # dp[i][j] -> (s2可以利用字符位置，s1可以利用的字符位置,它们之前共有字符串的ascii最大和)
        dp = [[(0,0,0) for _ in range(len(s1))] for _ in range(len(s2))]
        for x in range(len(s2)):
            for y in range(len(s1)):
                if y > 0:
                    c2, c1, c3 = dp[x][y-1]
                    tag = s2[c2: y+1].find(s1[y])
                    dp[x][y] = (c1+tag+1, c2, c3+s1[y] if tag != -1 else c3)
                if x > 0:
                    if dp[x][y][2] > dp[x-1][y][2]:

'''
# 官方py题解是py2的，不过算法懂了后代码就不重要了。dp的实现一直都不太难。