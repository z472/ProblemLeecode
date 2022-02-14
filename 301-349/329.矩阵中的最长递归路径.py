'''
虽然是困难题，但是操作很有限，不难理解算法。
官方题解二：拓扑排序上进行修改。

广度优先遍历，简单的dp思想，比周围最大的+1就是从当前出发的最长递增序列长度。结束的边界条件为
该结点的出度为0.这就和 有向图中拓扑排序 的方法很相近。

下面有代码分析。代码比它题解的文字好理解很多。
'''


class Solution:
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        rows, columns = len(matrix), len(matrix[0])
        outdegrees = [[0] * columns for _ in range(rows)]
        queue = collections.deque()
        for i in range(rows):
            for j in range(columns):
                for dx, dy in Solution.DIRS:
                    newRow, newColumn = i + dx, j + dy
                    # 各节点的出度值
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[i][j]:
                        outdegrees[i][j] += 1
                if outdegrees[i][j] == 0:
                    queue.append((i, j))

        ans = 0
        while queue:
            ans += 1
            size = len(queue)
            for _ in range(size):
                row, column = queue.popleft()
                for dx, dy in Solution.DIRS:
                    newRow, newColumn = row + dx, column + dy
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] < matrix[row][
                        column]:
                        outdegrees[newRow][newColumn] -= 1
                        if outdegrees[newRow][newColumn] == 0:
                            queue.append((newRow, newColumn))

        return ans
'''
它没用他推导的dp递推式，而是用了一个广度优先遍历的大局上的思考。我说的是ans。还有就是它用了一个队列来保存出度为0的结点。
它不是在出度矩阵outdegree中修改的。这样就减少了重复遍历的时间损耗。      还是理解ans的含义和出度为0队列为空的含义。就
能很好的复写下来这个题。 
'''
