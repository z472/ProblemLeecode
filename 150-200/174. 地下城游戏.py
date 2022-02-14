'''
https://leetcode-cn.com/problems/dungeon-game/solution/di-xia-cheng-you-xi-by-leetcode-solution/
推荐看官方上面的题解。动态规划要做到“无后效性”，也就是不能靠后遇到的数据来决定当前规划得到的最佳解，或是说二者不能有一点
联系。我下面正向DP到终点的算法，就是题解分析的那个毛病。当时思路出来的时候，我就很难构造出个例子来否定。想先编个程来提交
看看。但时间真的不允许多逗留了。题解的那个递推式注意理解  令dp[i][j]表示从坐标(i,j)到终点所需的最小初始值  这个概念。
其实还是好理解的。递推式写的很简洁。代码他也有对0行0列的处理，非常值得学下。

为何是反向DP能无后效性呢。粗略看法：是问题自身的特性。DP不管怎么弄都是要包括一个正确结果到最后。所以感觉是与递推的方向无关才对。

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        BIG = 10**9
        dp = [[BIG] * (m + 1) for _ in range(n + 1)]
        dp[n][m - 1] = dp[n - 1][m] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                minn = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(minn - dungeon[i][j], 1)

        return dp[0][0]

'''
from typing import List, Tuple

# 下面是错误版本。核心逻辑wrong。
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        line, row = len(dungeon), len(dungeon[0])
        eachline: List[Tuple[int, int]] = [(0, 0)] * row
        for i in range(line):
            for j in range(row):
                if i == j == 0:
                    eachline[j] = (dungeon[0][0], dungeon[0][0])
                elif j == 0:
                    eachline[j] = (min(eachline[j][0], eachline[j][1] + dungeon[i][j]), eachline[j][1] + dungeon[i][j])
                elif i == 0:
                    eachline[j] = (
                        min(eachline[j - 1][0], eachline[j - 1][1] + dungeon[i][j]), eachline[j - 1][1] + dungeon[i][j])
                else:
                    hisup = min(eachline[j][0], eachline[j][1] + dungeon[i][j])
                    hisleft = min(eachline[j - 1][0], eachline[j - 1][1] + dungeon[i][j])
                    if hisup == hisleft:
                        eachline[j] = (hisup, max(eachline[j][1], eachline[j - 1][1]) + dungeon[i][j])
                    elif hisup > hisleft:
                        eachline[j] = (hisup, eachline[j][1] + dungeon[i][j])
                    else:
                        eachline[j] = (hisleft, eachline[j - 1][1] + dungeon[i][j])
            print(eachline)
        return 1 if eachline[-1][0] >= 0 else 1 - eachline[-1][0]


mt = [[-5, -3, 3],
      [-5, -10, 1],
      [10, 30, -2]]
bug = [[1, -3, 3],
       [0, -2, 0],
       [-3, -3, -3]]
print(Solution().calculateMinimumHP(bug))
