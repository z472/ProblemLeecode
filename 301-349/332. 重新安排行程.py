'''
这种「一笔画」问题与欧拉图或者半欧拉图有着紧密的联系，下面给出定义：
通过图中所有边恰好一次且行遍所有顶点的通路称为欧拉通路。
通过图中所有边恰好一次且行遍所有顶点的回路称为欧拉回路。
具有欧拉回路的无向图称为欧拉图。
具有欧拉通路但不具有欧拉回路的无向图称为半欧拉图。

（逐步插入回路算法）Hierholzer 算法
    用于在连通图中寻找欧拉路径
当我们顺序地考虑该问题时，我们也许很难解决该问题，因为我们无法判断当前节点的哪一个分支是「死胡同」分支。
不妨倒过来思考。我们注意到只有那个入度与出度差为 1 的节点会导致死胡同。而该节点必然是最后一个遍历到的节点。
对于当前节点而言，从它的每一个非「死胡同」分支出发进行深度优先搜索，都将会搜回到当前节点。而从它的「死胡同」
分支出发进行深度优先搜索将不会搜回到当前节点。也就是说当前节点的死胡同分支将会优先于其他非「死胡同」分支入栈。
最后将会得到一个反序的欧拉通路。

这题还要我们输出字符顺序最小的欧拉通路，要贪心的选择，即该结点有多个路到不同结点，选择最小的结点。
这里用到优先队列（堆）了。查询O(1),维护O(logN)。关键的不在这里，而是上面的理解。

下面是官方的代码。
'''
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(curr: str):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)

        vec = collections.defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            heapq.heapify(vec[key])

        stack = list()
        dfs("JFK")
        return stack[::-1]


