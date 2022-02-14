'''
执行用时：52 ms, 在所有 Python3 提交中击败了37.64%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了56.64%的用户

没想出解法，看题解然后编写代码作为练习。
这题虽然用的是单调栈，但是这个结构没那么复杂或是难想。唯一的问题还是分析不出来用它的理由。不要把
过多目光投射到它上面去。

这题很好的一个推理思路很像写代码，从核心入手，不考虑什么特殊的边界条件，这里就是原字符串中出现一次
的字符要保留这个特殊条件。   它分析的是删除1次，而不是题目要求的多次。1次很好想。    然后可不可以
多次这么做呢？-> 完全可以 ->  处理边界条件

“退一步想问题”
'''
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        resttimes = Counter(s)
        sortstack = []
        for i in s:
            resttimes[i] -= 1
            if i in sortstack:
                continue
            times = 0
            if sortstack:
                times = resttimes[sortstack[-1]]
            while sortstack and times > 0 and i < sortstack[-1]:
                sortstack.pop()
                if sortstack:
                    times = resttimes[sortstack[-1]]
            sortstack.append(i)

        return ''.join(sortstack)

mt = ["cbacdcbc", "bcabc", '']
bug = ["ecbacba", "bbcaac"]
for i in mt+bug:
    print(i, '-> ', Solution().removeDuplicateLetters(i))
