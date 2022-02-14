from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[i][cursum] = [yes, no] yes表示加当前的Nums[i]值为cursum的
        # 个数，no是不加当前值且值为cursum的个数
        # dp[i][cursum](no) = dp[i-1][cursum][yes]+dp[i-1][cursum][no]
        # dp[i][cursum][yes] = dp[i][cursum-nums[i]][no]
        # 最后res = sum(dp[-1][target])
        if abs(target) > sum(nums) or (target + sum(nums))%2:
            return 0
        target = (target + sum(nums))//2
        print('add = ', target)
        dp = [[[0,0] for _ in range(target+1)] for i in range(len(nums))]
        if nums[0] < target+1:
            dp[0][nums[0]][0] = 1
        # 真的有点搞，下面这个逻辑,在测第一个用例中感受到的
        dp[0][0][1] = 1
        for i in range(1, len(nums)):
            for j in range(target+1):
                dp[i][j][1] = dp[i-1][j][0] + dp[i-1][j][1]
                if j >= nums[i]:
                    dp[i][j][0] = dp[i][j-nums[i]][1]
        print()
        for i in range(len(nums)):
            print(dp[i])
        return sum(dp[-1][target])

test = [[1,1,1,1,1], 3]     # 漏了一个起始赋值的逻辑
wrong1 = [[1000], -1000]    # 没有过滤好
wrong2 = [[0,0,0,0,0,0,0,0,1], 1]   # 其实赋值那里冗余的逻辑导致后面赋值把前面的覆盖了
wrong3 = [[7,9,3,8,0,2,4,8,3,9], 0]
# print(Solution().findTargetSumWays(*test))
# print(Solution().findTargetSumWays(*wrong1))
print(Solution().findTargetSumWays(*wrong3))