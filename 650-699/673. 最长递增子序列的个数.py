'''
这道题下面的代码是错误的，但是我最终的想法和官方题解的最优解：贪心 + 前缀和 + 二分查找
是完全一致的，数据结构也是完全一致，因为这个题目分析到最后就是唯一的一种方法。我没看懂它
的题解一，复杂度O(n^2)的算法。它说这第二种方法是在题解一上优化拓展得到的。可我是没看到
二者的联系。我是从计算最长递增子序列的过程中，想增加一些逻辑让它也能计算个数，还有就是下面
算法提交失败的一个用例[3,1,2]中发现我下面算法记录保存的数据有缺失。只能先是一个单调栈保存
当前的最长递增子序列d[i]，在每个d[i]下保存能成为i位置的历史值还有每个历史值当时对应的个数。
详细就看官方题解二，完全一致。 哦对了，我和它不一致的地方是，我居然没想到对数组d去二分，可以
看到我内循环是遍历stack。不过其实差不多。     这算法其实和蛮力差不多，只是用两个单调栈去
存储数据可以提高速度而已。分析到正确的时候，想要操作的逻辑非常直白了。不过我最初很难一下子分析
到最具“一般“（普适性）的情况。

把会某些数据修改成更一般情况。就是想的更全面些。

'''
from typing import List

# 下面代码逻辑有缺陷。
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        stack = [nums[0]]
        res = 1
        for idx in range(1, len(nums)):
            i = nums[idx]
            for jdx in range(len(stack) - 1, -1, -1):
                if i > stack[-1]:
                    stack.append(i)
                    break
                elif i == stack[-1]:
                    res += 1
                    break
                # 当stack长度为1，i < stack[-1]时，要替换stack[-1]值
                elif stack[-1] == stack[0]:
                    stack[-1] = i
                    res += 1
                if i > stack[jdx]:
                    stack[jdx + 1] = i
                    if i == stack[-1]:
                        res += 1
                    break

        return res


errortest = [[1, 3, 5, 4, 7], [2, 2, 2, 2], [1, 2, 4, 3, 5, 4, 7, 2], [2, 1], [3,1,2]]
for i in errortest:
    print('input:', i)
    print(Solution().findNumberOfLIS(i))
