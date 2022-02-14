'''
常见的dp题，和712有点相似，因为不是找两个数组的最长子序列而是子数组，要求共同部分是连续的。
所以dp[x][y]只需要知道dp[x-1][y-1]的值即可，就是说下面的代码是可以优化SC的。就是斜着
dp这个二维数组，这个过程可以用一维数组优化。     还有就是官方的第二种滑动窗口法，它的tc要比
dp大一些，但也可以使用，因为sc=O(1)。概括讲就是“对齐，一同向后遍历”，注意这个对齐并不重要，
即使首元素不相同也要向后遍历，它这个流程这个操作就是一个逻辑。也蛮好的。
'''
from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums1)+1)] for _ in range(len(nums2)+1)]
        rmax = 0
        for x in range(1, len(nums2)+1):
            for y in range(1, len(nums1)+1):
                if nums1[y-1] == nums2[x-1]:
                    dp[x][y] = dp[x-1][y-1] + 1
                    rmax = max(dp[x][y], rmax)
                else:
                    dp[x][y] = 0 #max(dp[x-1][y], dp[x][y-1])

        return rmax
'''
print('-----')
for i in dp:
    print(i)
print('-----')
'''
test = [([0,1,1,1,1],[1,0,1,0,1]), ]
for i in test:
    print(Solution().findLength(i[0],i[1]))