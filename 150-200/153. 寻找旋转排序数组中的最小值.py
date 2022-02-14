'''
执行用时：40 ms, 在所有 Python3 提交中击败了59.23%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了87.12%的用户
第二次过的。二分法而已。之前做过这个旋转数组是 查找 某个元素。这次改成最小值。
32ms代码如下：
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return nums[0]
        if nums[0]<=nums[-1]:
            return nums[0]
        begin, end = 0, len(nums) - 1
        while begin < end:
            mid = (begin + end) // 2
            if nums[mid]>=nums[0]:
                begin = mid + 1
            else:
                end = mid
        return nums[begin]
我和它的主要不同是while条件。我是如果是nums[rl] < nums[rr]就提前跳出nums[rl]。理应比它更快才对。
'''
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        rl, rr = 0, len(nums)-1
        while nums[rl] > nums[rr]:
            rmid = (rl+rr)//2
            if nums[rmid] > nums[rr]:
                rl = rmid+1
            else:
                rr = rmid   # bug rr = rmid-1

        return nums[rl]

mt = [[3,4,5,1,2], [4,5,6,7,0,1,2], [1], [4,6,7,0]]
bug = [[3,1,2]]
for i in bug+mt:
    print('in:', i)
    print(Solution().findMin(i))