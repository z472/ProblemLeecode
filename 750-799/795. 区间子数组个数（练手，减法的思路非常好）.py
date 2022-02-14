'''
执行用时：104 ms, 在所有 Python3 提交中击败了54.21%的用户
内存消耗：20.7 MB, 在所有 Python3 提交中击败了16.84%的用户
通过测试用例：46 / 46

有点挫折，bug点源于对不同情况想写在一个if下，某个变量的含义有些模糊，出现错误。

官方题解的思路非常好，将问题转化了，其实就是 减法，算最大值至少有一个在[left,right]的子数组，就是用在right以下的子数组个数
减去在left以下的子数组个数。这么说不如看题解的例子，0,1,2三种状态很清楚。

class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        def count(bound):
            ans = cur = 0
            for x in A :
                cur = cur + 1 if x <= bound else 0
                ans += cur
            return ans

        return count(R) - count(L - 1)

要求的数据从全局来看有包含关系。
'''
from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res, cur, curidx = 0, 0, 0
        for i in range(len(nums)):
            if left <= nums[i] <= right:
                if cur == 0:
                    curidx = i-1
                    for j in range(i):
                        if nums[i - j - 1] > right:
                            break
                        else: cur += 1
                cur += i - curidx
                curidx = i
                res += cur
            elif nums[i] < left and cur:
                res += cur
            else:
                cur = 0

        return res

test = [([1,0,1,2,1,4,3], 2, 3),]
wrong = [([2,9,2,5,6], 2, 8)]
for i in test+wrong:
    print(Solution().numSubarrayBoundedMax(*i))