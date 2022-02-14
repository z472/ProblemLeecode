'''
执行用时：6940 ms, 在所有 Python3 提交中击败了32.76%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了100.00%的用户
通过测试用例：61 / 61

woc,第一次有SC击败了100%的代码。这题难度不大，基本就是练手。

官方题解第二方法也是dfs,但第一种方法愣是看不懂。
'''
from collections import defaultdict
from itertools import product
from typing import List
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        d1 = defaultdict(list)
        for i in allowed:
            d1[i[:2]].append(i[2])
        def dfs(s):
            if (slen := len(s)) == 1:
                return True
            for i in range(slen-1):
                if s[i]+s[i+1] not in d1:
                    return False
            for i in product(*[d1[s[i:i+2]] for i in range(len(s)-1)]):
                i = ''.join(i)
                if dfs(i):
                    return True
            return False
        return dfs(bottom)

test = [("BCD",["BCC","CDE","CEA","FFF"]),]
for i in test:
    print(Solution().pyramidTransition(*i))