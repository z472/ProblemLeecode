'''
算法本身用蛮力一样的深度遍历也能通过，力扣上py有人这么写题解。
我的dfs有错误，就是在我的if第二个位置，我想的是能被第二次找大西洋也复用到，回头看这连第一次都不对
要是多建几个变量就可以，实现，但我真的是习惯性的不愿意加变量，“挑战自己”。发现根本不好写。

学学人家的BFS，啊这，看到一个DFS tc>100%,sc>80%且那个代码惨不忍睹。我服了这破题。
BFS代码抄在最下面了，没有官方出来，也不知道到底哪个更好。BFS更难想for me.
'''
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        c1 = [[0 for _ in range(n)] for _ in range(m)]
        res = []
        def dfs(x, y):
            c1[x][y] += 1
            if x > 0 and c1[x - 1][y] - c1[x][y] == -1 and heights[x - 1][y] >= heights[x][y]:
                dfs(x - 1, y)
            if y > 0 and c1[x][y - 1] - c1[x][y] == -1 and heights[x][y - 1] >= heights[x][y]:
                dfs(x, y - 1)
            if x < m-1 and c1[x + 1][y] - c1[x][y] == -1 and heights[x + 1][y] >= heights[x][y]:
                dfs(x + 1, y)
            if y < n-1 and c1[x][y + 1] - c1[x][y] == -1 and heights[x][y + 1] >= heights[x][y]:
                dfs(x, y + 1)

        # 到左上边界的太平洋
        for ydx in range(n):
            dfs(0, ydx)
        for xdx in range(m):
            dfs(xdx, 0)
        # 到右下边界的大西洋
        # for ydx in range(n):
        #     if c1[m - 1][ydx] == 1:
        #         dfs(m - 1, ydx)
        # for xdx in range(m):
        #     if c1[n - 1][xdx] == 1:
        #         dfs(n - 1, xdx)
        # for x in range(m):
        #     for y in range(n):
        #         if c1[x][y] == 2:
        #             res.append([x, y])
        print('---->>')
        for i in c1:
            print(i)
        return res

mt = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print('---->>')
for i in Solution().pacificAtlantic(mt):
    print(i, end='')
print('---->>')

'''
import collections
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def BFS(start):
            queue = collections.deque()
            queue.append(start)
            visited = set()
            visited.add(start)
            daxi = 0 # 用于检测是否到达大西洋
            taiping = 0  # 用于检测是否到达太平洋
            while queue:
                nx, ny = queue.popleft()
                for x, y in [(nx + 1, ny), (nx, ny + 1), (nx-1, ny), (nx, ny - 1)]:
                    if 0 <= x < len(heights) and 0 <= y < len(heights[0]) \
                        and heights[x][y] <= heights[nx][ny] and (x, y) not in visited:
                        queue.append((x, y))
                        visited.add((x, y))

                if nx == 0 or ny == 0:
                    taiping = 1
                if nx == len(heights)-1 or ny == len(heights[0])-1:
                    daxi = 1
                if daxi == 1 and taiping == 1:
                    return True
            return False
        #print(BFS((1,4)))
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if BFS((i, j)) == True:
                    res.append((i, j))
        return res
'''
