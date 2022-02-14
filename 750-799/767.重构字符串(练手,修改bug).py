'''
执行用时：52 ms, 在所有 Python3 提交中击败了6.92%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了53.03%的用户
通过测试用例：69 / 69

标记了两处bug点，尤其是第二bug，太低级了，哎。算法并不难想。我的代码可以算是官方题解二，基于计数的贪心，
但其实也不是很相似，看它啰嗦了很多，代码也比我长，准备写个题解。
'''
from collections import Counter
from functools import reduce
class Solution:
    def reorganizeString(self, s: str) -> str:
        d1 = Counter(s)
        resortlist = [(k,v) for k,v in d1.items()]
        resortlist.sort(key=(lambda x:x[1]),reverse=True)
        n = resortlist[0][1]
        if len(s)-n < n-1:
            return ""
        # bug 1
        x = [[resortlist[0][0],] for _ in range(n)]
        t = -1
        for i in range(1, len(resortlist)):
            ch, times = resortlist[i]
            for j in range(t+1, 1+t+times):
                x[j%n].append(ch)
            # bug 2
            t = j
        return ''.join(list(reduce((lambda z,y:z+y),x)))

test = ['aabv','aaab']
wrong = ["vvvlo","xxxxxuuuppp"]
for i in test+wrong:
    print(Solution().reorganizeString(i))