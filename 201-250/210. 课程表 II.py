'''
执行用时：184 ms, 在所有 Python3 提交中击败了5.74%的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了43.26%的用户
当然我看了题解，但只是看了拓扑排序的概念和操作。
第三次过的。第一次输入空列表。第二次是outdegree初始化少了东西导致字典找不到key

·当字典找不到key的时候，解释器的输出为 KeyError: 3 这里3就是没有key=3的键值对。

官方题解：深度优先遍历。和很久之前那些递归的那些“排列组合”类似的题目代码有点像。
别看代码比我长，还有递归，而我只有迭代。但是我要每个操作都要做O(n)维护入度字典。总的复杂度为O(n^2)。
这个题 如果像我模仿 输出拓扑排序结果的方法--找入度为0的结点，进入附近结点，删除之前过来入度0的结点，再循环这过程，
继续寻找入度为0。是很自然的。
但它去深度遍历，通过三个状态来判断是否遍历过，开始时为任意一个 未搜索 的结点，每层递归就是for 循环该结点的相邻结点，
并把该结点的状态改成 搜索中， 当然第一次循环每个都是递归下去，然后都回溯了for结束可以把该结点给标记为 搜索结束 状态。

递归要是能把时间复杂度直接降低一个维度，那绝对是好递归。 有的递归是可以用栈存储来迭代实现，就不是好的递归尝试。
这个递归思路很隐蔽，和它设计的记录状态的数组结合很紧密。后者使他更加隐蔽。不过如果认为它是一个 图 的题。那么DFS和BFS
就应该是条件反射一样的反应过来。
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 存储有向图
        edges = collections.defaultdict(list)
        # 标记每个节点的状态：0=未搜索，1=搜索中，2=已完成
        visited = [0] * numCourses
        # 用数组来模拟栈，下标 0 为栈底，n-1 为栈顶
        result = list()
        # 判断有向图中是否有环
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal valid
            # 将节点标记为「搜索中」
            visited[u] = 1
            # 搜索其相邻节点
            # 只要发现有环，立刻停止搜索
            for v in edges[u]:
                # 如果「未搜索」那么搜索相邻节点
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                # 如果「搜索中」说明找到了环
                elif visited[v] == 1:
                    valid = False
                    return
            # 将节点标记为「已完成」
            visited[u] = 2
            # 将节点入栈
            result.append(u)

        # 每次挑选一个「未搜索」的节点，开始进行深度优先搜索
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        if not valid:
            return list()

        # 如果没有环，那么就有拓扑排序
        # 注意下标 0 为栈底，因此需要将数组反序输出
        return result[::-1]
'''
from typing import List


class Solution:
    def findzero(self, d: dict) -> int:
        for i in d:
            if d[i] == 0:
                return i
        return -1

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]
        # 初始化两个字典。
        indegree = {i: 0 for i in range(numCourses)}
        outdegree = {}
        ret = []
        for i in prerequisites:
            outdegree.setdefault(i[1], []).append(i[0])
            indegree[i[0]] += 1

        for _ in range(numCourses):
            x = self.findzero(indegree)
            if x == -1:
                return []
            indegree[x] = numCourses
            ret.append(x)
            # 最慢的地方就是维护indegree字典，每次都为O(n)
            for i in outdegree[x]:
                indegree[i] -= 1
        return ret


mt = [4, [[1, 0], [2, 0], [3, 1], [3, 2]]]
bug = [3, [[1,0]]]
print(Solution().findOrder(mt[0], mt[1]))
print(Solution().findOrder(bug[0], bug[1]))
