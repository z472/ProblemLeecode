'''
执行用时：52 ms, 在所有 Python3 提交中击败了64.34%的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了12.19%的用户
错了一次，tc=O(n).sc=O(n)。巧了它的总和也用的单词 total。循环写的都有点像。
官方题解：和我tc一样的方法是经典的 滑动窗口(双指针)。这样的sc=O(1)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1

        return 0 if ans == n + 1 else ans
'''
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        from collections import deque
        sav = deque()
        total, minlen = 0, len(nums)+1
        for i in nums:
            if total < target:
                sav.append(i)
                total += i
            if total >= target:     # 漏了=号
                for j in range(len(sav)):
                    total -= sav.popleft()
                    if total < target:
                        minlen = min(minlen, len(sav)+1)
                        break
        return 0 if minlen == len(nums)+1 else minlen

mt = ([1,1,1], 7)
bug = ([1,2,3,4,5],15)
print(Solution().minSubArrayLen(mt[1], mt[0]))
print(Solution().minSubArrayLen(bug[1], bug[0]))