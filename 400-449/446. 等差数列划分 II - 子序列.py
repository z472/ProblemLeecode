'''
这题的题解讲了一个不算难理解的DP还有一个就是官方很pythonic的代码了。

虽然tc和sc都是O(N*N)。但它题目没有对输入列表有限制，无序，整数。它
说len(input)在1000以下。这个数据量上看也默许了这个复杂度。我有点反
敢这么的算法，自己想的时候有过类似的dp,但还想看看有无更加好的。总是
在这里纠结~~
'''
from typing import List


class Solution_sonice:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        f = [defaultdict(int) for _ in nums]
        for i, x in enumerate(nums):
            for j in range(i):
                d = x - nums[j]
                cnt = f[j][d]
                ans += cnt
                f[i][d] += cnt + 1
        return ans

