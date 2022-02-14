'''
执行用时：36 ms, 在所有 Python3 提交中击败了95.95%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了59.79%的用户

惊！ 蛮力法站起来了！
'''
from typing import List
from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = Counter(nums1), Counter(nums2)
        return list((n1&n2).keys())

mt = [[4,9,5], [9,4,9,8,4]]
print(Solution().intersection(mt[0], mt[1]))