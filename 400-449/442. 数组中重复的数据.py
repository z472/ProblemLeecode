'''
执行用时：112 ms, 在所有 Python3 提交中击败了43.31%的用户
内存消耗：21.2 MB, 在所有 Python3 提交中击败了16.16%的用户

这个是符合题意的，不用额外空间且tc=O(1)。但是代码还可以优化一下。

注意它的题意它数组的每个值都是在1~n（n为数组长度）的。故如果想把每个值i放到对应的nums[i-1]中，出现一次
和两次就能看到不同。  这题也是计数排序的一种变形个人感觉。 代码之前有重复输出值。后面填了几个多余操作。并不
快速。
'''
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        idx = 0
        res = []
        while idx < len(nums):
            i = nums[idx]
            if i < 0:
                idx += 1
                continue
            if i != nums[i-1]:   # 把一个值放到它对应的位置，该位置第一次有合适的值
                nums[idx], nums[i-1] = nums[i-1], nums[idx]
            elif idx != i-1:    # 把一个值放到它对应的位置，该位置第二次有合适的值
                res.append(i)
                nums[idx] = -i
                idx += 1
            else:               # 一个值已经在正确位置上
                idx += 1
        return res

T1 = [4,3,2,7,8,2,3,1,]
print(Solution().findDuplicates(T1))


