'''
我第一个版本就是官方题解的Sc=O(1).就是直接切片后面的k个值放到前面去。但是我觉得第一个的
写法不优雅。之前也有写过列表分段  解包  的写法。但是当k大于len(nums)出现了偶数返回为[]的bug。奇数居然不会
'''
from typing import List

'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]
'''

# ???
class Solution:
    def rotate(self, nums, k):
        nums[:k % len(nums)], nums[k % len(nums):] = nums[-(k % len(nums)):], nums[:-(k % len(nums))]
        return nums


mt = [1, 2, 3, 4, 5, 6, 7]
bug = [1]  # nums为一个元素上面的bug出在了偶数上面。不知为何？奇数偶数%1都是0，为何偶数就会返回[]
k = [2]
for i in k:
    print('k=', i)
    print(Solution().rotate(bug, i))
