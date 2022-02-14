'''
执行用时：44 ms, 在所有 Python3 提交中击败了32.80%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了83.32%的用户
通过测试用例：48 / 48

这是官方题解二，也是比较快的算法，排序+dp。     想了一会把题，转为了状态值的dp。
'''
from collections import Counter
from typing import List
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        record = [[x,times] for x,times in Counter(nums).items()]
        record.sort()
        deleted, undeleted = 0, 0
        for i in range(len(record)):
            x,times = record[i]
            if x == record[i-1][0]+1:
                deleted, undeleted = undeleted + x*times, max(deleted, undeleted)
            else:
                undeleted = max(deleted, undeleted)
                deleted = undeleted + x*times
        return max(deleted, undeleted)