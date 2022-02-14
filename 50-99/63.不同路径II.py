'''
    用了两个相似的递归，第一个是比第二个能减少点递归，但是对于29行，18列的测试用例无能为力，
不会运行得到结果，也没有报错。只能去看官方题解了，思路也是动态规划，通过修改数据来得到最终结果
官方没有python的，以下是一个py3的题解的代码，运行超过了11%，占用空间超过了45%，不过占用其实
区别就是你在输入里改还是自己建个二维列表，没什么东西，主要是它写的太pythonic了
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):

        # 定义状态：即数据元素的含义：dp表示当前位置的路径条数
        # 建立状态转移方程：dp[i] = dp[i]+dp[i-1]
        # 设定初始值：增加初始值1，即dp = [1] + [0]*n
        # 状态压缩：即优化数组空间,将二维数组压缩到一维数组,逐行计算当前最新路径条数，并覆盖上一行对应的路径条数
        # 选取dp[-2]表示到达finish位置路径总条数,因为一开始新增加的1,因此最终值要往前推一个

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1] + [0]*n
        for i in range(0,m):
            for j in range(0,n):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j]+dp[j-1]
        return dp[-2]
'''

class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid):
        # obstacleGrid: List[List[int]]) -> int:
        # 避免不必要的计算
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        def child(r, l):
            a1 = 0
            if r >= 1 and obstacleGrid[r - 1][l] != 1:
                a1 += child(r - 1, l)
            if l >= 1 and obstacleGrid[r][l - 1] != 1:
                a1 += child(r, l - 1)
            obstacleGrid[r][l] = '1' if r == 0 and l == 0 else str(a1)
            return int(obstacleGrid[r][l])

        return child(m - 1, n - 1)


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid):
        # obstacleGrid: List[List[int]]) -> int:
        global sum, a, b
        sum = 0
        a, b = len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1

        def child(x, y):
            global a, b, sum
            if x == a and y == b:
                sum += 1
                return
            if x > a or y > b or obstacleGrid[x][y]:
                return
            child(x + 1, y)
            child(x, y + 1)

        child(0, 0)
        return sum

ab = Solution1()
mytest = ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0], [0, 1], [0, 0], [0, 0]], [[0, 1], [0, 0]])


def ct(m, n, obstacles=[]):
    res = [[0 for _ in range(n)] for _ in range(m)]
    for i in obstacles:
        res[i[0]][i[1]] = 1
    return res


obsta = [(1, 2), (0, 6), (3, 3), (2, 0)]
lee_test = [ct(4, 7, obsta), ct(3, 3, ([2, 1], [1, 2]))]
l1 = [[[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
       [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
       [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]], ]
for i in l1:
    print('in:')
    for j in i:
        print(j)
    print(ab.uniquePathsWithObstacles(i))
    for j in i:
        print(j)
