'''
执行用时：540 ms, 在所有 Python3 提交中击败了5.43%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了65.12%的用户

这题不难，就是练练手。代码还可以优化，但是这个内存占用是有点小啊，这里用过不少拼接字符串。
这题最尴尬的是很少有人去写，提交少的可怜。
'''
class Solution:
    def magicalString(self, n: int) -> int:
        s = '12'
        if n < 4:
            return 1
        sint = 3
        while len(s) < n:
            if len(s) < sint:
                ss = ''
                for i in range(len(s)):
                    sint += ((i%2)+ 1)*int(s[i])
                    ss += str((i%2)+ 1)*int(s[i])
                s = ss

        return s[:n].count('1')
