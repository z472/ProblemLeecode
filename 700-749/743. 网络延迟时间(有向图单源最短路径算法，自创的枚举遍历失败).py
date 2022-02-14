'''
我代码在没有逻辑表达错误的第22个用例的时候出错。嗯，应该就是算法的纰漏，看这题解的第一行描述就知道错了，
这是一个成熟的算法，Dijkstra 算法，它上来就说：将所有节点分成两类：已确定从起点到当前点的最短路长度的节点，
以及未确定从起点到当前点的最短路长度的节点。这是你算法逻辑的漏洞。

有时间看这个算法的详细题解。简单看了下，这是算法课上老师讲过的经典题，还是有两个人两种办法的。
https://leetcode-cn.com/problems/network-delay-time/solution/wang-luo-yan-chi-shi-jian-by-leetcode-so-6phc/
'''
from collections import defaultdict, deque
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # bfs
        record = defaultdict(list)
        # ntimes字典保存曾经作为出发点的结点当时的最短时间
        ntimes = {k: 0}
        for i in times:
            record[i[0]].append(i[1:])
        print(f'record={record}')
        curlist = deque([k])
        while curlist:
            i = curlist.popleft()
            cur = ntimes[i]
            for j in record[i]:
                if j[0] not in ntimes:      # 当ntimes.get(j[0]) = 0 判断就会出错，常见bug了
                    ntimes[j[0]] = cur + j[1]
                else:
                    ntimes[j[0]] = min(ntimes[j[0]], cur + j[1])
                curlist.append(j[0])
            del record[i]
        print(f'ntimes={ntimes}')
        if len(ntimes.keys()) < n:
            return -1
        return max(ntimes.values())

test = [([[2,1,1],[2,3,1],[3,4,1]], 4, 2), ([[1,2,10],[1,3,1],[3,4,2],[2,4,1],[4,2,1]], 4, 1)]
wrong = [([[1,2,1],[2,1,3]],2,2),
         ([[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]],5,3)]
# for i in test+wrong:
#     print(Solution().networkDelayTime(*i))
print(wrong[1][0].__len__())