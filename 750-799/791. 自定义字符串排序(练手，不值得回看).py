'''
执行用时：32 ms, 在所有 Python3 提交中击败了72.44%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了86.22%的用户
通过测试用例：39 / 39

这题算是简单题了，无语。、
'''
from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d1 = Counter(s)
        res = ''
        for ch in order:
            if d1.get(ch, None):
                res += ch*d1[ch]
            del d1[ch]
        for ch in d1:
            res += d1[ch]*ch
        return res