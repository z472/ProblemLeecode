'''
执行用时：112 ms, 在所有 Python3 提交中击败了8.72%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了88.57%的用户

dfs啊这。
'''
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        tag = 2
        def four(x,y):
            res = []
            for i,j in ((0,1), (0,-1), (1,0), (-1,0)):
                if 0<= x+i < len(grid) and 0<= y+j < len(grid[0]):
                    if grid[x+i][y+j] == 1:
                        res.append((x+i,y+j))
            return res
        maxareas = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs = []
                cur = grid[i][j]
                area = 0
                if cur == 1:
                    dfs.append((i,j))
                    while dfs:
                        x,y = dfs.pop()
                        area += 1
                        grid[x][y] = 2
                        dfs += four(x, y)
                        for i,j in four(x,y):
                            grid[i][j] = 2
                maxareas = max(maxareas, area)

        return maxareas

test = [[[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]],
[[1,1,0,0,0],
 [1,1,0,0,0],
 [0,0,0,1,1],
 [0,0,0,1,1]]
]
for i in test[1:]:
    print(Solution().maxAreaOfIsland(i))
