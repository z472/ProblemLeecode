'''
卡在了第267个输入（全部是269个输入），卡在了一个45长度的字符1上，我的算法也很一般感觉，是观察题目然后“分隔”一些确定不会是
连起来形成2位数的点，然后是计算那些可以随意捏合的数，比如是12122，任意相邻两位都可以组成2位数，又由于它们是一段一段的，可以
把每个结果相乘得到最后方法数。但在45个1上，看来这个计算是错误的，公式我根据间隔，靠了点排列组合推导的，是代码的下面部分。但
为啥能对267个呢，该算法真的是计算公式不对吗？
官方题解：无
下面是之前很经典的那个“走楼梯”那个题（可以转化为斐波那契数列，后来又用了什么快速幂运算减到logn复杂度），这里也是那个动态规划
就可以，而且思路和走楼梯几乎一样。也就是说你以后可以多转化下题目看看能不能用到之前的算法的内容。那个人的代码写的也比较不错，对
于x0的判断还有错误的判断，都使你的思路远离那个方法。但下面代码很好的处理了那些特殊判断。即使我的算法是对的，效率由于要遍历一遍
数据并保存，加上后续复杂度n^2的计算公式。还是不如它这个优雅。
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n==0: return 0
        dp = [1,0]
        dp[1] = 1 if s[0]!='0' else 0
        for i in range(1,n):
            dp.append(0)
            if s[i]!='0':
                dp[i+1] += dp[i]
            if s[i-1:i+1]>='10' and s[i-1:i+1]<='26':
                dp[i+1] += dp[i-1]
        return dp[-1]
下面代码是错的。QAQ.
'''
class Solution:
    def numDecodings(self, s):
        # s: str) -> int:
        sav = []
        pre, end, res = 0, 0, 1
        while end <= len(s)-1:
            if s[end] == '0':
                return 0
            if int(s[end:end+2]) > 26:
                sav.append((pre, end))
                pre = end + 1
                end += 1
            elif int(s[end:end+2]) in [10, 20]:
                sav.append((pre, end-1))
                end = pre = end + 2
            else:
                end += 1
        sav.append((pre, end-1))
        print(sav)
        # 计算公式，长度为n+1,有n个间隔，然后最多有a=(n+1)//2 a个2位数存在，它们这段的总的解码方法是
        # sum = n + 1/2*( (n-1)*(n-2) + (n-2)*(n-3) + 2*[()+()] + 3*[()+()] + ··· + (a-1)*[2*1] )
        for i in sav:
            if i[0] < i[1]:
                x, n = 0, i[1] - i[0]
                # a = (n + 1) // 2
                for j in range(1, n - 1):
                    x += ((n - 1) * (n - 2)) * ((j + 1) // 2)
                    n -= 1
                x = x // 2
                x += i[1] - i[0] + 1
                print(i, '->', x)
                res *= x
        return res
a = Solution()
mt = ['122327121', '12202221020']
leetest = ['12', '226', '0', '06', '111111']
wrongtest = "111111111111111111111111111111111111111111111"
print(len(wrongtest))
# for i in leetest[:]:
#     print('in:', i)
#     print(a.numDecodings(i))