'''
执行用时：44 ms, 在所有 Python3 提交中击败了51.77%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了40.12%的用户

本来以为是dp智商检测题，结果成了编程能力检测题。
收尾时错了很多，提交也错了两次。

'''
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        offset, ans = 0, 1
        last = nums[0]
        for cur in nums:
            if (cur - last) * offset < 0:
                ans += 1
            if cur - last != 0:
                offset = cur - last
            last = cur
        return ans+1 if ans > 1 or nums[-1] != nums[0] else ans

mt = [[1,3,5,4,2,3], [1,7,4,9,2,5], [1,17,5,10,13,15,10,5,16,8], [1,2,3,4,5,6,7,8,9]]
bug = [[84], [0,0], [1,3,5,5,4,4]]
for i in mt+bug:
    print(i, Solution().wiggleMaxLength(i))

