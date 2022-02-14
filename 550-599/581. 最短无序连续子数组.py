'''
执行用时：40 ms, 在所有 Python3 提交中击败了98.48%的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了65.14%的用户

这道题题目要求用O(n)，也算是提示了。随着对题目的分析理解，最后发现贪心算法很好解决问题。
从左向右遍历找到“需要”交换的最右结点。向左亦然。 嗯，贪心就是这样，往往想出来后代码没什
么可写的。

题解居然说可以一次遍历，结果就是把我两个方向的循环写成了一个循环而已，没有任何本质的区别，
这种写法我觉得很不好，不过确实可以那么做。

本题官方题解1，思路是全部排序后，对比前后两个数组，哪个位置不一致。这种对比虽然是O(nlogn)但是很新颖。
'''
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        minidx, maxidx = 0, 0
        oncemax = nums[0]
        for i in range(1, len(nums)):
            if oncemax > nums[i]:
                minidx = i
            else:
                oncemax = nums[i]
        oncemin = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if oncemin < nums[i]:
                maxidx = i
            else:
                oncemin = nums[i]
        return minidx - maxidx + 1 if minidx != maxidx else 0
