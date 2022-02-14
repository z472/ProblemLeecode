class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[0,0] for j in range(n)] for i in range(m)]
        dire = [(0,1),(1,0),(-1,0),(0,-1)]
        # 蛮力法。bfs,tc=O(m*n*maxMove),移动步骤多的自动替换前面某位置移动次数较少的,
        # dp数组的值表示在移动了x步时某一个位置的路径数，由于数据会覆盖，所以要设置新老两个
        res = 0
        for i in range(maxMove):
            pass
            # 看了官方题解，也是这种方法，还自称dp，感觉就是蛮力法。我发现个问题，常常在想解法的时候不会
            # 站在最基本的地方去想，总想上来就是一个不错复杂度的，想了很多发现最基础的版本。
            # 很多低复杂度都是在这上面一步步优化的，不过这道题确实无法优化。但是可以发现计算机的强力之处。
            # 很能计算。
            # 有兴趣可以写写。    这道题一看题目哇很有趣哦，不定流程，不定输出，感觉很牛。

