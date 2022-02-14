'''
官方题解：观察这个运算：n & (n-1)，其运算结果恰为把 n 的二进制位中的最低位的 1 变为 0 之后的结果。
就考虑倒数2位就能理解。如果n为奇数，后两位为x1 & x0 之后的结果为 x0。n为偶数，10 & 01 = 00
它的逻辑推理更重要。既然这个运算是这个 ”效果“ 。做一次消一个1，那么最后数就为log2(n)位的0。
class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n:
            n &= n - 1
            ret += 1
        return ret
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        sumone = 0
        while n:
            if n & 1:
                sumone += 1
            n = n >> 1
        return sumone
