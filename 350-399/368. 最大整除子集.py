'''
执行用时：372 ms, 在所有 Python3 提交中击败了52.53%的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了5.01%的用户

虽然是表现很差，但是好在是中等难度，深度优先遍历+记忆化，且完全自己探索，且是一次过的。
'''
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        lennums = len(nums)
        sav = [0] * lennums  # nums同位置的最长路径列表
        start = [1] * lennums  # 可能的起始点

        def dfs(idx: int) -> List[int]:
            # 遍历能整除nums[idx]的下一个值，且这些值之间不能整除
            ret = []
            for i in range(idx + 1, lennums):
                if nums[i] % nums[idx] == 0:
                    if sav[i] == 0:     # 记忆化
                        dfs(i)
                    start[i] = 0
                    if len(sav[i]) > len(ret):
                        ret = sav[i]
            sav[idx] = [nums[idx]] + ret
            return sav[idx]

        ret = []
        for i in range(lennums):
            if start[i] == 1:
                if len(dfs(i)) > len(ret):
                    ret = sav[i]
        # print(sav, start)
        return ret

mt = [[1, 2, 8, 4, 3], [2, 3, 5, 15, 12, 6],[2,4,8,12,30,33,36,72]]
for i in mt:
    print(i, end=' ')
    print(Solution().largestDivisibleSubset(i))
