'''
犹豫了30分钟，是建立一个完整的1对1映射的数据结构，让每个键值对可以O(1)直接查出来的那种。
那样就需要考虑从输入的列表中，向一个部分正确的结构中添加。还有怎么把两个值域比如先是ab,cf两个值域，然后来个
bc输入。怎么把两个值域的全部结果都和另一个值域的结点连接上。emmmmm感觉不好写。

然后就是分析出有结果的就是连在一个连通图中的。画了下图。决定还是走递归遍历的方法。

执行用时：32 ms, 在所有 Python3 提交中击败了94.94%的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了97.54%的用户

一次过好评。bug不多，主要是传参有点多，忘了一个两个就出错了。感觉利用递归去遍历，然后只在正确时传出一个值。这里处理的很好。
'''
from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 建立字典key是每个结点，键是该结点在equations中直接挨着的其他结点
        nodes = defaultdict(dict)  # 它可以容纳多个连通图
        ans = []
        for idx, x in enumerate(equations):
            i, j = x
            nodes[i][j] = values[idx]
            nodes[j][i] = 1 / values[idx]

        def dfs(track: List) -> None:
            # track为轨迹列表，记录着遍历过的所有结点，不走之前的轨迹，走所有一个边连着的
            # 结点。可能会走到死胡同，但如果是在一个连通图中的结点，总会走到的。
            nonlocal savrighttrack
            cur = track[-1]
            if cur == target:
                savrighttrack = track  # 可不可以不切片，可以
                return
            for i in nodes[cur]:
                if i not in track:
                    dfs(track + [i])

        for i, j in queries:
            savrighttrack = []
            target = j
            if i not in nodes:  # 起点是未知结点
                ans.append(-1.0)
                continue
            dfs([i])
            v = 1.0
            if savrighttrack:
                for x in range(len(savrighttrack) - 1):
                    v *= nodes[savrighttrack[x]][savrighttrack[x + 1]]
            elif i != j:
                v = -1.0
            ans.append(v)
        return ans


mt = [[["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]]
for i in mt:
    print(i)
print()
print(Solution().calcEquation(mt[0], mt[1], mt[2]))
