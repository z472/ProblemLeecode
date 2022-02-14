'''
一次过的ok
执行用时：48 ms, 在所有 Python3 提交中击败了91.62%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了73.75%的用户

解题思路：我向63题的题解的动态规划的思路来写，可以说是很好的解决了它，如果
是递归的话，排列组合数的值会是巨量的，0 <= m,n <= 200.组合数的遍历情况
太多太多了。这里为何可以用双层循环来实现呢，就是贪心遍历+动态规划（DP的基础
就是它题里的最短路径是只限向右和向下的，如果是四个方向随意走，我觉得就无法用
一个列表来存储每行的值来DP了），贪心按道理是不能求出正确结果的，但是把每行每
个位置都贪心一遍，就可以得到最优值。

代码方面：在if...elif...这里写的不错，这个语法类似C的case...switch
然后就把频率高的放前面，这里还不错。
'''
class Solution:
    def minPathSum(self, grid):
        # grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        sav = [0]*n
        for i in range(m):
            for j in range(n):
                if i and j:
                    sav[j] = min(sav[j-1], sav[j]) + grid[i][j]
                elif not i and not j:
                    sav[j] = grid[i][j]
                elif not i:
                    sav[j] = sav[j-1] + grid[i][j]
                elif not j:
                    sav[j] = sav[j] + grid[i][j]
        return sav[-1]

a = Solution()
mytest = ([[1,3,1],[1,5,1],[4,2,1]], [[1,2,3],[4,5,6]])
for i in mytest:
    print('in:')
    for j in i:
        print(j)
    print(a.minPathSum(i))