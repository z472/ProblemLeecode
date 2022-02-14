print('''十分十分难过的一道题，提交一顿错，错误频出。原因1：从特例来总结出的算法不正确，好多都没考虑到
好在及时放弃另想方法，没有再在上面修改。原因2：最初编写后来看的逻辑错的算法时，还发现了切片的错误，各种边界的错误，语法不熟
原因3：很多不细致考虑的算法，会让你以为就是最后正确的。原因4：最初写的时候，有一种边写边看的心态''')
class Solution:
    def divide(self, dividend, divisor):
        ch = '+'*2
        if dividend < 0:
            ch = '-+'
            dividend = str(dividend)[1:]
        elif dividend > 0:
            dividend = str(dividend)
        else:
            return 0
        if divisor < 0:
            ch = ch[0]+'-'
            divisor = str(divisor)[1:]
        else:
            divisor = str(divisor)
        if len(divisor) > len(dividend) or int(divisor) > int(dividend):
            return 0
        oupt = ''
        for i in range(len(dividend)):
            b = dividend[:i+1]
            c = 0
            while int(b) >= int(divisor):
                b = str(int(b)-int(divisor))
                c += 1
            oupt += str(c)
            if c != 0:
                if b == '0':
                    dividend = ''.join(['0' for j in range(i+1)]) + dividend[i+1:]
                else:
                    dividend = ''.join(['0' for j in range(i+1-len(b))]) + b + dividend[i+1:]

        if ch[0] == ch[1]:
                if int(oupt) > 2**31-1:
                    return 2**31-1
                else:
                    return int(oupt)
        else:
            return -int(oupt)

a = Solution()
test = [(20, 3), (-2039, 11), (1237, 12), (-2**31, 1), (27670, 23), (2147483647, 2)]
for i in test[:6]:
    print(a.divide(i[0], i[1]))

print(1073741823)