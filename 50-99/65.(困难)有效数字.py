'''
执行用时：44 ms, 在所有 Python3 提交中击败了63.83%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了24.08%的用户
提交错了一次，没注意到符号要在首位上，总之改的挺快的，写的也还顺利。学习下
官方题解：有限状态自动机，它是一个计算模型，它包含一系列状态，有一个特殊的
状态，被称作「初始状态」。还有一系列状态被称为「接受状态」，它们组成了一个
特殊的集合。其中，一个状态可能既是「初始状态」，也是「接受状态」。自动机驱
动的编程，可以被看做一种暴力枚举方法的延伸：它穷尽了在任何一种情况下，对应
任何的输入，需要做的事情。自动机在计算机科学领域有着广泛的应用。在算法领域，
它与大名鼎鼎的字符串查找算法「KMP」算法有着密切的关联；在工程领域，它是
实现「正则表达式」的基础。
'''
class Solution:
    def isNumber(self, s):
        # s: str) -> bool:
        '''
        小数：（可选）正负号，必有一个点，然后点两边必有一位数字即可
        整数：（可选）正负号，必有一位数字
        有效数字：小数或整数，或是他俩加个e/E然后加个整数
        '''
        def f_i_judge(s, tag):
            # tag得0为整数，得1为小数
            ssign, snumb, sdot = 0, 0, 0
            for i in s:
                if '0' <= i <= '9':
                    snumb += 1
                elif i == '+' or i == '-':
                    ssign += 1
                elif i == '.':
                    sdot += 1
                else:
                    return 0  # 直接退出，不是有效
                if ssign > 1 or sdot > 1:
                    return 0
            if snumb == 0 or (ssign == 1 and s[0] not in ['+', '-']):
                return 0
            return 1 if sdot == tag else 0
        eindx = max(s.find('e'), s.find('E'))
        if eindx == -1 and f_i_judge(s, 1) or f_i_judge(s, 0):
            return True
        elif (f_i_judge(s[:eindx],0) or f_i_judge(s[:eindx],1)) and f_i_judge(s[eindx+1:], 0):
            return True
        return False

a = Solution()
mt1 = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
mt2 = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
mt3 = ['3e4e-2', '0e+-3', '--2.4e0', '5+3']
for i in mt3:
    print(i, a.isNumber(i))