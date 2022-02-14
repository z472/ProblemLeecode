'''
方法：构造
如何避免枚举 [1,2,...,n] 的排列呢，需要我们观察一些特殊的用例：

顺序数组或者逆序数组：[1,2,3,...,n] ，呈等差数列形式，此时公差为 1，即 k=1；
最大值和最小值交错出现： [1,n,2,n−1,3,n−2,....]，此时相邻的两个数的差的绝对值不会出现重复，k 达到最大，k=n−1。
大家可以用一个具体的例子验证一下。

当 n=6 和 k=3 时，可以构造数组 [1,2,3,6,4,5] 是符合要求的，如何得到它们呢？
构造等差数列： [1，2]，此时题目中给出的差的列表为 [1]；
构造交错数列：[1，4，2，3]，此时题目中给出的差的列表为 [3,2,1]，再给每个元素加 2，得到 [3，6，4，5]。
于是得到了算法。

从两个特殊归纳出一般的解法。逻辑性比较强。很吃“组合_利用信息的能力”

我下面的算法纯是没有正确性把握的构造。和官方题解相似的地方是都是想先把k个差值放好，再放后面的值。但是放k个差值的方式
简直天壤之别。我后面放值就会产生巨大的复杂度，需要回退（下面写的还没有这个点）
'''
import collections
from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        if k >= n:
            return []
        ret = collections.deque([n, ])
        restset = set(range(1, n))
        for diff in range(k, 0, -1):
            i = (ret[-1] - diff) if (ret[-1] - diff) > 0 else ret[-1] + diff
            if i in restset:
                restset.remove(i)
            ret.append(i)
        while restset:
            j = restset.pop()
            if abs(ret[-1] - j) <= k:
                ret.append(j)
            elif abs(ret[0] - j) <= k:
                ret.appendleft(j)
            else:
                return [0,0]
        return ret

test = [(4,2),(5,2),(8,2)]
for n,k in test:
    print('n=',n,' k=',k)
    print(Solution().constructArray(n, k))