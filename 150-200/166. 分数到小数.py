'''
执行用时：44 ms, 在所有 Python3 提交中击败了37.34%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了91.70%的用户
四次才过。编码在循环那里进度缓慢。测试不充分，一提交都是bug。符号问题，负数整除正数的下去整问题。
官方题解：需要用一个哈希表记录余数出现在小数部分的位置，当你发现已经出现的余数，就可以将重复出现的小数部分用括号括起来。
下面是一个28ms的提交。了解到新的divmod函数。还有他把 余数和输出数组长度 做了一个映射，很不寻常的想法。这样做确实使过
程变的更单调了。而且循环退出的两个条件，商==0和余数是否在之前存储过，是必要的判断，每次都要做两次。但他把商为0的情况多
了些处理，使得函数的出口只有连接res中的字符。看上去很优雅。

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0:
            return "0"
        res = []
        if (numerator>0) ^ (denominator>0):
            res.append("-")
        numerator,denominator = abs(numerator),abs(denominator)

        # a-商，b-余数
        a,b = divmod(numerator,denominator)
        res.append(str(a))
        if b==0:
            return "".join(res)
        res.append(".")

        loc = {b:len(res)}
        while b:
            a,b = divmod(b*10,denominator)
            res.append(str(a))
            if b in loc:
                res.insert(loc[b],"(")
                res.append(")")
                break
            loc[b] = len(res)
        return "".join(res)
'''
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        savremainder, sign = [], 1
        if numerator < 0:
            numerator, sign = -numerator, -sign
        if denominator < 0:
            denominator, sign = -denominator, -sign
        if numerator % denominator == 0:
            return str(numerator // denominator * sign)
        res = '-' if sign < 0 else ''
        res += str(numerator // denominator) + '.'
        # 保留小数部分的商
        savquotient = []
        remainder = numerator % denominator
        # remainder = remainder * 10 // denominator
        while remainder != 0 and remainder not in savremainder:
            # 上一次的余数
            savremainder.append(remainder)
            # 当前一次
            savquotient.append(str(remainder * 10 // denominator))
            remainder = remainder * 10 % denominator

        if remainder == 0:
            return res + ''.join(savquotient)
        else:
            x = savremainder.index(remainder)
            return res + ''.join(savquotient[:x]) + '(' + ''.join(savquotient[x:]) + ')'

mt = [(1,2), (2,1), (2,3), (4,333), (1,5)]
bug = [(1,6), (50, 8), (-50, 8), (-23, 1)]
for i in mt+bug:
    print('in:', i)
    print(Solution().fractionToDecimal(i[0], i[1]))
