'''
建议直接看官方题解，只有一个并不复杂的dp算法，我下面的dfs不知道哪里出问题，卡在了第22个测试用例上，
记得是直接输出错误。正常来讲，是否超时是最大的麻烦，因为它要求最便宜，在k中转站内，就必须是要遍历全部
情况。     官方是状态dp，已经是最好的情形了。
'''
from typing import List
from collections import defaultdict
from functools import lru_cache
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d1 = defaultdict(list)
        for i in flights:
            d1[i[0]].append(i[1:3])
        cur = []
        @lru_cache()
        def dfs(begin, end, k):
            nonlocal cur
            minfee = float("inf")
            if begin == end: return 0
            if k == 0: return -1
            for i in d1[begin]:
                if i[0] not in cur:
                    cur.append(i[0])
                    fee = dfs(i[0], end, k-1)
                    cur.pop()
                    if fee == -1:
                        continue
                    minfee = min(minfee, fee+i[1])
            return minfee if minfee != float("inf") else -1
        return dfs(src, dst, k)