'''
执行用时：228 ms, 在所有 Python3 提交中击败了11.93%的用户
内存消耗：20.8 MB, 在所有 Python3 提交中击败了92.49%的用户
虽然这题的速度不快，但是难得是一次过，我的方法搜索会遇到很多边界值。
我最初的操作是官方题解里的 缩小搜索空间。但我没有递归进行，我是递归做的，找到左下右上两个可能解空间，然后
再次利用某个小于target值的左上部分和右下部分不是解这个特性去搜索。

看了官方题解最后一个，也是最好的那个。看似很简单的操作确实蕴含丰富。矩形的路线问题，之前也做过一个困难的DP，
要去除算法的 后续性。就是要反过来去DP。174题。  这次的算法也是取了矩形的一个角入手，不同于一般的左上角入手。
在简单的操作中，蕴含了很多，且不丢解。要善于发现、多观察。
'''
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 先向右下方向行进到拐点a，然后根据情况去左下和右上去搜索。
        if matrix[0][0] > target:
            return False
        m, n = len(matrix), len(matrix[0])
        a = 0
        for i in range(min(m, n)):
            if matrix[i][i] >= target:
                a = i
                break
        else:
            a = min(m, n) - 1
        if matrix[a][a] == target:
            return True
        x = a
        print('拐点', (x, x))

        for y in range(a+1, 0, -1):
            x -= 1
            while x + 1 < m:
                if matrix[x + 1][y - 1] == target:
                    return True
                if matrix[x + 1][y - 1] < target:
                    x += 1
                else:
                    break
            if x == m-1:
                break

        y = a
        for x in range(a+1, 0, -1):
            y -= 1
            while y + 1 < n:
                if matrix[x - 1][y + 1] == target:
                    return True
                if matrix[x - 1][y + 1] < target:
                    y += 1
                else:
                    break
            if y == n - 1:
                break


matrix = [[1, 5, 8],
          [2, 7, 10],
          [6, 11, 14],
          [9, 16, 20],
          [19, 21, 23]]
mt = [1, 3, 2, 11, 6, 16, 21, 9, 19,20]
rightup = [5, 8, 10, ]
# for i in mt+rightup:
#     print('target=', i, ' ', Solution().searchMatrix(matrix[:2], i))
#     print()
print(Solution().searchMatrix(matrix[:2], 8))