'''
执行用时：28 ms, 在所有 Python3 提交中击败了98.54%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了23.23%的用户

这题，也是中等难度？？
'''
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        lena, lenb = len(a), len(b)
        for i in range(3):
            if b in a*(lenb//lena+i):
                return lenb//lena+i
        return -1