'''
执行用时：40 ms, 在所有 Python3 提交中击败了11.97%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了73.75%的用户
通过测试用例：52 / 52

这代码是最简化的逻辑了。这道题隐含的数据信息非常多。哦，看了官方代码，它居然和我思路不一样，
我比它还要复杂了。       它只记录了一个当前遍历的最大数，遍历到i时，看最大数是否是i。

class Solution(object):
    def maxChunksToSorted(self, arr):
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i: ans += 1
        return ans

我的curmax不只是当前遍历的最大数，还包括了应该达到的最大数，我里面多了个i,对比着理解的话它的ma就是当前
遍历过的这i个数中的最大数。

为什么可以省略这个i。
'''
from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res, curmax = 1, arr[0]
        for i in range(len(arr)):
            curmax = max(curmax, i, arr[i])
            if i == curmax:
                res += 1
        return res - 1

test = [[4,3,2,1,0], [1,0,2,3,4], [0,2,1]]
for i in test:
    print(Solution().maxChunksToSorted(i))