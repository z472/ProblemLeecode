'''
要理解负数如何和整数相加需要明白一个“溢出”的概念。
4位有符号数，它能表示的是[-8,7] 16个数。负数一律按补码处理，即正数取反，末位+1。
比如：-2 + 3
    1110（-2）
    0011
=(1)0001    最前面的1因为“溢出”被吃掉了。所以有符号数相加需要设置数值的位数限制。而py又是弱类型语言，
数字声明不用说是int或是long等等类型。
    下面的编码和你编码思路可以说是完全不同，它是有一个 无进位相加作为基础。（注释是我加的）
    下面代码像加密电报一样难以破解，他做了简化操作，不是完全版。

class Solution:
    def getSum(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF     # 0x十六进制，相当于截取了后32位，因为它是二进制的32个1
        b &= 0xFFFFFFFF     # 但我觉得这里没啥用，&1不就是它自己吗。
        while b:
            carry = a & b
            a ^= b      #  a获取的是a,b的无进位加法的结果.它以后就不是输入的a了。
            b = ((carry) << 1) & 0xFFFFFFFF
            # print((a, b))
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)     #  如果最后为负数的补码就转化成负数

'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        ret = (a&1)^(b&1)
        carrybit = 0
        i = 0
        while a or b or carrybit:
            a1, b1, c1 = a & 1, b & 1, carrybit
            carrybit = 0
            if a1 ^ b1 ^ c1:    # 有奇数个的1， 1,3
                ret |= 1 << i
                carrybit = a1 & b1 & c1
            elif a1 | b1 | c1:
                carrybit = 1
            i += 1
            a, b = a >> 1, b >> 1
        return ret


mt = [(6,2), (7,1),(4,2),(-1,-3)]
for i in mt[:]:
    print(i, Solution().getSum(i[0], i[1]))
