'''
https://leetcode-cn.com/problems/reverse-bits/solution/dian-dao-er-jin-zhi-wei-by-leetcode/
看官方题解的后两者解法：直接爆炸。位运算熟练者写的东西就像怪物一样。
法一法二的思路：我也有，但是不会不用bin()（它可以把int转为前缀位0b的二进制字符串）的纯位运算写法。
'''
'''
法一:n & 1取最后一位，左移power位是模拟二进制数其实是2**a，最后还有ret += ...是把高位保留下来然后合成一个结果。
'''


class Solution:
    def reverseBits(self, n):
        # 题目说了是32位无符号整数，故power最大31
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret


'''
代码还可以每次只取出末位值然后每次让ret << 1,但实际题目要求是在32位中去”颠倒“。
就是你原来是1,颠倒过来值应该位2**31。下面的代码就是错的。
'''


class SolutionWrong:
    def reverseBits(self, n):
        ret = 0
        while n:
            ret += (n & 1)
            ret, n = ret << 1, n >> 1
        return ret >> 1
'''
法二：不懂整个算法。
'''

class Solution2:
    def reverseBits(self, n):
        ret, power = 0, 24
        cache = dict()
        while n:
            ret += self.reverseByte(n & 0xff, cache) << power   # 0xff = 2**8-1, 0b11111111
            n = n >> 8
            power -= 8
        return ret
    # 在这里，我们展示一种完全基于算术和位操作，不基于任何循环语句.
    def reverseByte(self, byte, cache):
        if byte not in cache:
            cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023
        return cache[byte]

'''
法三：不使用循环来反转32位值。（逐渐狂暴）
解释说是分治。评论有说它不应算作常规解题方法。
'''
class Solution3:
    def reverseBits(self, n):
        n = (n >> 16) | (n << 16)   # 把32位数分成两半，取或，就是相同的位不动，保存不同的位置
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n

x = 12
mt = [12, 10, 7]
for x in mt:
    print(x, ' ', bin(x))
    y = Solutionb().reverseBits(x)
    print(y, ' ', bin(y))
