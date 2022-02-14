'''
class Solution(object):
    def numTilings(self, N):
        MOD = 10**9 + 7
        dp = [1, 0, 0, 0]
        for _ in xrange(N):
            ndp = [0, 0, 0, 0]
            ndp[0b00] = (dp[0b00] + dp[0b11]) % MOD
            ndp[0b01] = (dp[0b00] + dp[0b10]) % MOD
            ndp[0b10] = (dp[0b00] + dp[0b01]) % MOD
            ndp[0b11] = (dp[0b00] + dp[0b01] + dp[0b10]) % MOD
            dp = ndp

        return dp[0]

这题虽然是dp，但我更觉得是找到一个不重复的铺砖累加的方法。我找的方法是末尾添加一个独立的块，但是会漏一些
情况，我甚至都不清楚是什么样的情况。反正我找的规律并没有普适性和也不是很科学，实现也很累，所以这种找规律题
以后还是不要发现什么东西就想着用，还没发现最最本质的规律。       官方的代码也很有意思，索引那里用0bxx
二进制来写，还有就是 取模运算的性质，最后的dp[0]是由前面的相加得到的，所以可以对前面的状态也取模，这样四个
变量不会特别大。
'''
class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[1], dp[0] = 1, 1
        for i in range(2,n+1):
            cur = 0
            for j in range(1, i+1):
                if j < 3:
                    cur += dp[i-j]
                elif j == 4 or j == 3:
                    cur += 2*dp[i-j]
                elif (j-3)%2:
                    continue
                else:
                    cur += 2*dp[i-j]
            dp[i] = cur
        return dp[-1]

test = [i for i in range(2, 10)]
for i in test:
    print(f'i={i},', Solution().numTilings(i))