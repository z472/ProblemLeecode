'''
题目：给定一个字符串 s，找到 s 中最长的回文子串。你可以假设s的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：
输入: "cbbd"
输出: "bb"
'''
class Solution:
    def longestPalindrome(self, s):
        # babcdcbaabcd -> bab , abcdcba, dcbaabcd
        # 1.遍历寻找起点i，判断和i相同的字母组成的字符串，有点慢。
        # 2.找最大可以从长到短的考虑，而且两端必是相同字母才是回文串（有的长度没有，可以跳过一些），而且一旦找到就是最大长度
        '''
        提交过了，但是官方题解里的三个方法没一个是我这么做的。而且运行时间是2500ms。
        '''
        totall = len(s)
        for l in reversed(range(1, totall+1)):
            # l = len(s) : s[:1],
            for idx, i in enumerate(s[:1+totall-l]):
                if s[idx+l-1] == i:
                    k = l//2
                    print(l, ':', s[idx:idx + k], '<->', s[idx+l-k:idx + l])
                    if s[idx:idx+k] == s[idx+l-k:idx+l][::-1]:
                        return s[idx:idx+l]
            if l == 1:
                return -1

s_list = ['babcdcbaabcd', 'bab', 'bb', 'b']
a = Solution()
for i in s_list:
    print(a.longestPalindrome(i))
    print('-------------')




