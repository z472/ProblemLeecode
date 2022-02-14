'''
执行用时：40 ms, 在所有 Python3 提交中击败了56.69%的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了89.96%的用户
一次过，但是没啥意义，单纯是因为忘了杨辉三角第n项的求法，就是二项式公式的系数、可以O(n)。
官方题解的O(n)也是这个数学算式。
'''
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]*(rowIndex+1)
        x, y = rowIndex, 1
        for i in range(1, rowIndex+1):
            res[i] = x//y
            x *= (rowIndex-i)
            y *= (i+1)
        return res

Solution().getRow(7)