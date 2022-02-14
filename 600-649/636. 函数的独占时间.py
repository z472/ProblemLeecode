'''
执行用时：36 ms, 在所有 Python3 提交中击败了95.08%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了8.20%的用户通过
测试用例：120 / 120

题目的细节导致出错，还有就是漏掉操作（丢逻辑）。官方题解看了也是栈。就是模拟题目描述的流程。
'''
from typing import List
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        startstack = [] # [val] val = [id,time]
        res = [0 for _ in range(n)]
        for i in logs:
            funid, operate, timestp = i.split(":")
            funid, timestp = int(funid), int(timestp)
            if operate == 'start':
                if startstack:
                    lastid, lasttime = startstack[-1]
                    res[lastid] += timestp - lasttime
                startstack.append([funid,timestp])
            else:
                # end对应的id默认为startstack的最后一个的id
                res[funid] += timestp - startstack[-1][1] + 1
                startstack.pop()
                if startstack:
                    startstack[-1][1] = timestp + 1
        return res

T = [(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]), ]
for n,log in T:
    print(log,'\n', Solution().exclusiveTime(n, log))


