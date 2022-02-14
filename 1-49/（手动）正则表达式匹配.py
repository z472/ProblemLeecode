class Solution:
    def pisExist(self, p):  # 模式字符串是否必定含有1到多个字符
        sum = 0
        for i in p:
            if (i<'z' and i>'a') or i=='.':
                sum += 1
            elif i == '*':
                sum -= 1
        if sum <= 0:
            return False
        else:
            return True
    def isMatch(self, s, p):
        sx, px=0, 0
        ls, lp = len(s), len(p)
        for idx, i in enumerate(p):
            if sx == ls:  # p还至少有一个字符，但s遍历到尽头的情况，此时的sx超出了索引的范围,这行就是先行判断
                if self.pisExist(p[idx:]):
                    return False
            if i <= 'z' and i >= 'a':
                if idx==lp-1 or p[idx+1] != '*':    # p该位是字符后面不跟*号情况
                    if sx==ls or s[sx] != i:
                        return False
                    else:
                        sx += 1
                elif p[idx+1]=='*':     # 后面跟*号
                    if s[sx]!=i:
                        pass
                    else:
                        # for m in range(len(s[sx:])-1):
                        #     if self.isMatch(s[sx + m:], p[idx + 2:]):
                        #         return True
                        # if m == len(s[sx:]) - 2:
                        #     return False
            elif i == '.':
                if idx != lp-1 and p[idx + 1] == '*':  # p='.*aa'类似这种，*号不知道遍历多少个s的字符
                    if idx+2<lp:    # .*后面还有字符
                        for k in range(len(s[sx:])-1):      # 表示.*取代了0到ls-2，给传入的s最少留一个字符
                            if self.isMatch(s[sx+k:], p[idx+2:]):
                                return True
                        if k == len(s[sx:])-2:
                            return False
                    else:
                        return True
                else:   # 正常情况遍历一个s字符
                    sx += 1
        if sx==ls:      # 此时p全部遍历完，且没退出，sx超出索引说明也正常遍历完s了。
            return True
        else:
            # print('1')
            return False

a = Solution()
s1 = [('ab', 'ab.*'), ('aab', 'c*a*b'), ('aa', 'a'), ('aa', 'a*'), ('aaa', 'aaaa'), ('aaaa', 'a*a')]
s2 = [('aaab', '.*c'), ('aab', '.*c*a*b'), ('aaab', '.*')]
s3 = [('cccccdf', 'c.*dff'), ('cccccdf', '.*c.*df'), ('ab', 'ab.*'), ('adfsdf', '.*')]
for i in s1:
    print(a.isMatch(i[0], i[1]))