'''
执行用时：424 ms, 在所有 Python3 提交中击败了96.09%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了72.89%的用户

啊这。。。一次过，这题真的是解了也是暴力法的改良而已啊。啊这。。。
'''
from collections import defaultdict
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d1, d2 = defaultdict(int), defaultdict(int)
        for i in nums1:
            for j in nums2:
                d1[i+j] += 1
        for x in nums3:
            for y in nums4:
                d2[x+y] += 1
        res = 0
        for a in d1:
            if d2.get(-a):
                res += d1[a]*d2[-a]
        return res
