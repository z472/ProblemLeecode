'''
执行用时：36 ms, 在所有 Python3 提交中击败了91.00%的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了97.73%的用户
没啥东西。就是练练编码，官方也没有题解。
'''
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res, n = 0, 0
        for i in range(len(columnTitle)-1, -1, -1):
            res += 26**n * (ord(columnTitle[i])-64)
            n += 1
        return res

mt = ['A', 'Z', 'AB', 'ZY', 'FXSHRXW']  # 2147483647
for i in mt:
    print(repr(i))
    print(Solution().titleToNumber(i))


