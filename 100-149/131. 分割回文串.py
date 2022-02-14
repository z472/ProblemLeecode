'''
执行用时：188 ms, 在所有 Python3 提交中击败了22.21%的用户
内存消耗：30.7 MB, 在所有 Python3 提交中击败了65.51%的用户
这题卡在唯一的逻辑判断那里很久，菜到自己了。运行和编码过程一样慢。
官方题解一：      回溯 + 动态规划预处理
没看懂它的“预处理”代码，也没懂为何要预处理。
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        ret = list()
        ans = list()

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return

            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret
'''
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sav = []
        le = len(s)
        def cd(k:int):
            lecur = 1
            while k+lecur <= le:
                half = (lecur+1)//2
                # 下面这行逻辑多次失败
                if list(reversed(s[k:k+half])) == list(s[k+lecur-half:k+lecur]):
                    sav.append(s[k:k+lecur])
                    if k+lecur == le:
                        res.append(sav[:])
                    else:
                        cd(k+lecur)
                    sav.pop()
                lecur += 1

        cd(0)

        return res
mt = ['aaab', ' ', 'aaaa', 'bababab', '']
for j in mt:
    for i in Solution().partition(j):
        print(i)
    print()