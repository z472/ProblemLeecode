'''
https://leetcode-cn.com/problems/combination-sum-iv/solution/zu-he-zong-he-iv-by-leetcode-solution-q8zv/
终于有官方题解了，然而我不会做。令我感到难受的dp。它这个题的难点在处理排列顺序的不重复。当然如果思路和
官方一样，也这个烦恼了。这题的dp有一个特性，就是有点蛮力法的影子，它有点像计数排序。它的dp结构是按所求值的
大小来的，这就会有很多空间占用。当然我想不出更好的方案。
'''
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]

        return dp[target]


# 作者：LeetCode - Solution
