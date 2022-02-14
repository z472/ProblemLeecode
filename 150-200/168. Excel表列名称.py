# 你的版本 对于701 -> ZY 的输出为 A@Y。对于676（26^2）的输出为A@@。
# 在分析了同样的算法但是循环中  执行顺序  不同的代码后，修改好了我自己的版本。
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        a, b = divmod(columnNumber, 26)
        while a != 0:
            if b == 0:
                res += 'Z'
                a -= 1
            else:
                res += chr(b+64)
            a, b = divmod(a, 26)
        res = chr(b+64) + res[::-1]
        return res[1:] if res[0] == '@' else res
'''
此题要复习的话，先去看题目。理解好再看。
此题是26进制的变体。正常求x进制就是 除x取余法。但它还有一个关键变化点，把0给去掉了，把x这个值放到后面。
如果单讲把数字和输出做映射，1 -》 A这种很简单。但你要做的是 把0映射到Z且让后面的除数a（题解里是n）要少
一个26. 因为这个除x取余法的核心就是模拟一个从低位到高位迭代运算的过程，如果想把当前位的值 手动+1，就相
当于借了前一位的大小为1的值来。这也是竖式减法常用的思路。

class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n:
            n, y = divmod(n, 26)
            if y == 0:
                n -= 1
                y = 26
            res = chr(y + 64) + res
        return res
'''

mt = [28, 1, 3]
bug = [701, 26, 26**2, 2147483647]
for i in mt+bug:
    print('in:', i)
    print(Solution().convertToTitle(i))

print("2147483647的答案:FXSHRXW")
