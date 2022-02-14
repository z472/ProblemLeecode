'''
执行用时：368 ms, 在所有 Python3 提交中击败了60.61%的用户
内存消耗：16.7 MB, 在所有 Python3 提交中击败了32.73%的用户
通过测试用例：52 / 52

这题分析可以从让一个字符串x判断是否为s的子序列的方法入手，肯定就是遍历s，另一个指针指向x，贪心地比较移动
指针位置。n个字符串x一起判断也是一样，除了要更复杂的数据结构。    我的代码一次过，觉得写的不错，初始化，
x中独有的字符的处理，最内层循环，都考虑不错。官方代码是py2，写法差不多。
'''
from collections import defaultdict
from typing import List
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d1 = defaultdict(list)
        lenlist = [len(i) for i in words]
        for i in range(len(words)):
            d1[words[i][0]].append((i,0))
        res = 0
        for i in s:
            t = []
            for j in d1[i]:
                if j[1]+1 < lenlist[j[0]]:
                    if (ch := words[j[0]][j[1]+1]) == i:
                        t.append((j[0],j[1]+1))
                    else:
                        d1[ch].append((j[0],j[1]+1))
                else:
                    res += 1
            d1[i] = t
        return res