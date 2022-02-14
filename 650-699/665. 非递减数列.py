'''
执行用时：40 ms, 在所有 Python3 提交中击败了70.79%的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了6.58%的用户

这题只是练手（编码）
'''
from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        pre1, pre2 = nums[0], nums[1]
        tag = 0 if pre1 <= pre2 else 1
        for i in nums[2:]:
            if i >= pre2:
                pre1, pre2 = pre2, i
            elif i >= pre1 and tag < 1:
                pre2 = i
                tag += 1
            else:
                tag += 1
            if tag == 2:
                return False
        return True
'''
优化了一个冗余判断
执行用时：32 ms, 在所有 Python3 提交中击败了95.55%的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了68.47%的用户
'''
class Solution2:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        pre1, pre2 = nums[0], nums[1]
        tag = 0 if pre1 <= pre2 else 1
        for i in nums[2:]:
            if i >= pre2:
                pre1, pre2 = pre2, i
            elif i >= pre1:
                pre2 = i
                tag += 1
            else:
                tag += 1
            if tag == 2:
                return False
        return True
