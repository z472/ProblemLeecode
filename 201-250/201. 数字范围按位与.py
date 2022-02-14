'''
执行用时：72 ms, 在所有 Python3 提交中击败了34.44%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了11.67%的用户

已知的事实是从left到right为0的位会被&成结果的0位。
·我主要是观察到了当left，right的二进制长度一样时默认首位都为1。
·若right的二进制位比left结果连续与会为0
·只有l < r < 2**n时才会有不为0的结果。然后就是我可以获得首位的值嘛，然后不断缩小left和right

官方题解：
1.公共前缀。他这个方法也是题目本质的揭露。在他不那么有说服力的证明之后，我勉强接受了他的这个转化。 答案就是left和right的公共前缀问题。
具体操作就是右移直到二者相等，然后再回退同样的距离就是答案了。
2.利用一个技巧Brian Kernighan 算法--n 和 n-1按位与之后，n的最后一个1会变成0.他的主思路还是两个输入的公共前缀，但是这次编码用这个
技巧来写。
两段代码如下：
1.
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        # 找到公共前缀
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift

2.
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:    # 这里不是线性的迭代，n在循环里是每次都在抹零而且它要比 2**x 的缩小还要快
            # 抹去最右边的 1
            n = n & (n - 1)
        return n
他们都是tc = log2(n), sc = O(1)。但使用Brian技巧的算法，n可以避开0，可以提速。

相比于编码，它把问题化简成求二者的公共前缀的过程更值得回味。
'''
from typing import List


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        n = len(bin(left)) - 2 - 1
        if left == 0 or right >= 2**(n+1):
            return 0
        return 2**n + self.rangeBitwiseAnd((left-2**n), (right-2**n))

mt = [(5, 7), (29, 31)]
for i in mt:
    print('in:', i)
    print(Solution().rangeBitwiseAnd(i[0], i[1]))