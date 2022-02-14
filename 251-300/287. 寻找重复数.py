'''
执行用时：36 ms, 在所有 Python3 提交中击败了95.43%的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了90.76%的用户
不会做，下面写的是官方题解的 快慢指针 解法。和141，142判断是否成环。准确是和142一样。
但它之前做的转化分析是。。。对 nums 数组建图，每个位置 i 连一条 i→nums[i] 的边。由于存在的重复的数字 target，因此 target
这个位置一定有起码两条指向它的边，因此整张图一定存在环。

官方还有两种tc稍微慢些的方法。二分法和二进制。都和索引有点关系。不好理解。
'''
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        i = 0
        while nums[i] != nums[fast]:
            i = nums[i]
            fast = nums[fast]
        return nums[i]

mt = [2,1,3,4,2]
print(Solution().findDuplicate(mt))