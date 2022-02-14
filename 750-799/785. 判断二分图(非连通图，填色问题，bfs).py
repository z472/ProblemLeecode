'''
执行用时：56 ms, 在所有 Python3 提交中击败了14.04%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了83.40%的用户
通过测试用例：80 / 80

除了调试阶段那个bug,笔误，绝对的笔误，有点搞笑。这题很像填色问题，只有两个颜色，让相邻结点不为同一种颜色。
我就bfs看是否有冲突，最外层循环针对非连通图。

官方题解居然也拿涂色做说明哦，看下官方的bfs代码：
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n

        for i in range(n):
            if color[i] == UNCOLORED:
                q = collections.deque([i])
                color[i] = RED
                while q:
                    node = q.popleft()
                    cNei = (GREEN if color[node] == RED else RED)
                    for neighbor in graph[node]:
                        if color[neighbor] == UNCOLORED:
                            q.append(neighbor)
                            color[neighbor] = cNei
                        elif color[neighbor] != cNei:
                            return False

        return True

它用队列deque来实现的，它的bfs是以每一个结点的角度，没有我当前层和下一层的设定，它是保留颜色，我是保留下一层的新节点，稍有区别。
'''
from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        l = [-1 for _ in range(len(graph))]
        '''
        0 - 1-5- 3 -4        
        | 
        2
        '''
        for i in range(len(graph)):
            if l[i] == -1:      # 这里bug了一下，马虎写成了graph[i] == -1
                l[i] = i % 2
                curlev = graph[i]
                while curlev:   # bfs，给当前层涂色，并加入没上色过的结点作为下一层
                    nextlev = []
                    color = (i+1) % 2
                    i += 1
                    for v in curlev:
                        if l[v] == -1:
                            l[v] = color
                            nextlev += graph[v]
                        elif l[v] != color:
                            return False
                    curlev = nextlev
        return True

test = [[[1,2,3],[0,2],[0,1,3],[0,2]], ]
for i in test:
    print(Solution().isBipartite(i))