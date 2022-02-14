'''
执行用时：100 ms, 在所有 Python3 提交中击败了35.70%的用户
内存消耗：18.8 MB, 在所有 Python3 提交中击败了19.35%的用户
一次过，但是算是蛮力法了，tc = klogk。但官方说用最小堆的方法是 klogn。貌似是因为这个堆最大为n个值。

官方的最优方法是非常有创造性的 二分法。它利用最大值和最小值和的一半作为x，然后“充分”利用矩阵性质，
    以O(n)复杂度求出了比x小的值的个数。这个操作很秀。
求出两个范围嘛。然后又以它作为边界值，在新的范围中重复上述过程。
每次寻找比x小的个数是O(n)，次数是O(log(max-min))。总复杂度为O(nlog(max-min))。不占用额外空间。

时间复杂度来讲，用堆的方法，最坏情况是n^2logn，本质还是蛮力法。而它就很稳定nlogC。log后面的都很小。

我看到官方题解的二分法，想了一会，居然没有想到统计数量来算不超过多少个值这点。
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

作者：LeetCode-Solution
'''
from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        h1 = [[matrix[0][0], 0, 0]]
        while True:
            if k == 1:
                return h1[0][0]
            x, y = h1[0][1], h1[0][2]
            if y == 0 and x < n - 1:
                heapq.heappush(h1, [matrix[x + 1][y], x + 1, y])
            if y < n - 1:
                heapq.heappushpop(h1, [matrix[x][y + 1], x, y + 1])
            else:
                heapq.heappop(h1)
            k -= 1


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = [1, 4, 6, 7, 9]
for i in k:
    print(i, '-> ', Solution().kthSmallest(matrix, i))
