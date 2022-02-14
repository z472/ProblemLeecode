'''
执行用时：4476 ms, 在所有 Python3 提交中击败了14.16%的用户
内存消耗：21.2 MB, 在所有 Python3 提交中击败了13.82%的用户


'''
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        dp = [[[_],] for _ in nums]

        for i in range(1, len(nums)):
            cur = []
            for j in range(i):
                if nums[j] <= nums[i]:
                    cur += [_ + [nums[i]] for _ in dp[j]]
            dp[i] += cur
        res = []
        for dpi in dp:
            if dpi:
                res += dpi
        t = []
        for i in res:
            if len(i) > 1 and i not in t:
                t.append(i)
        return t



test = [[4,6,7,7], [4,4,3,2,1]]
for i in test:
    print('i:', i,'\n', Solution().findSubsequences(i))
