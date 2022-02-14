'''
    对竖式乘法的改良一是避免重复乘，把n2之前某一位和n1乘的结果保存在sav里，这样再遇到时直接从中提取即可。88ms，运行击败67%还可以
看了官方题解，发现自己算是违规了，他们的相加是用字符串实现的，我是int类型转化了。
    不过好消息是，题解二做乘法的思路，是我之前考虑过的，（n1,n2长度为m,n)结果长度为(m+n)或（m+n+1），
然后建字符串数组保存结果，还要注意进位。
'''
class Solution:
    def multiply(self, num1, num2):
        # num1: str, num2: str) -> str:
        sav = dict(zip(range(1, 10), [-1 for _ in range(9)]))
        sav[0] = 0
        output = 0

        def com(num1, ch):
            res = 0
            for i in range(len(num1)):
                res += int(num1[-i - 1]) * int(ch) * 10 ** i
            return res

        for i in range(len(num2)):
            if sav.get(int(num2[-i - 1])) == -1:
                sav[int(num2[-i - 1])] = com(num1, num2[-i - 1])
            output += sav[int(num2[-i - 1])] * 10 ** i
        print('sav:',sav)
        return repr(output)


a = Solution()
mytest = [('33', '6'), ('123','456')]
for i in mytest:
    print('num1:', i[0], ' num2:', i[1])
    print('outp=', a.multiply(i[0], i[1]), 'result=',int(i[0])*int(i[1]))
