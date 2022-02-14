'''
执行用时：1788 ms, 在所有 Python3 提交中击败了  5.09%  的用户
内存消耗：18.4 MB, 在所有 Python3 提交中击败了71.00%的用户
之前做过类似的一个题264丑数II。我没看那个题，凭记忆来做，知道当时是标记每个质数位置指针的方法。但即使是入手了，
在dp过程中的操作我也是错误的，因为dp的初始含义就没有搞懂。这个含义是需要借助观察出的规律来敢于这么设计。就是注释
的内容。这个规律简单讲就是sav左边的值没乘的质数它右边的值也不会乘。

提速版本：612ms实现代码不同 关键就是利用了 列表生成式 这个语法来加速。
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        index = [0]*len(primes)
        dp = [1]+[0]*(n-1)

        for i in range(1, n):
            tmp = [dp[c]*primes[j] for j, c in enumerate(index)]
            res = min(tmp)
            dp[i] = res
            for k,l in enumerate(tmp):
                if l == res:
                    index[k] += 1

        return dp[-1]
'''
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        sav = [1] * n

        k = len(primes)
        # 在sav中没乘上这k个数的位序最小值
        tagidx = [0] * k
        for i in range(1, n):
            minnium = sav[tagidx[0]] * primes[0]
            for j in range(2 * k):
                index = j % k
                x = sav[tagidx[index]] * primes[index]
                minnium = min(minnium, x)
                if j >= k and x == minnium:
                    tagidx[index] += 1
            sav[i] = minnium
        # print('sav:', sav)
        return sav[-1]


mt = [(12, [2, 7, 13, 19])]
for i in mt:
    print('input:', i)
    print(Solution().nthSuperUglyNumber(i[0], i[1]))
