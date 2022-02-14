'''
执行用时：44 ms, 在所有 Python3 提交中击败了35.50%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了39.99%的用户
没有特例的去写，而是复用之前198.打家劫舍的代码实现的。理解的还是不错的。
官方题解：无
'''
from typing import List


class Solution:
    def rob1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        noadd, add = 0, 0
        for i in nums:
            add, noadd = noadd+i, max(add, noadd)
        return max(add, noadd)

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 4:
            return max(nums)
        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))

bug = [200,3,140,20,10]
mt = [bug,]
for i in mt:
    print('in:', i)
    print(Solution().rob(i))