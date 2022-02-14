'''
官方题解：分析出3种做法。法二：计算因子5的个数，法三：更好的计算5的个数。
https://leetcode-cn.com/problems/factorial-trailing-zeroes/solution/jie-cheng-hou-de-ling-by-leetcode/
抓住问题后置0的成因由2,5相乘得到的。且2必多于5.故有一个5就会有一个后置0.
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        sumfive = 0
        while n > 0:
            n //= 5
            sumfive += n
        return sumfive
