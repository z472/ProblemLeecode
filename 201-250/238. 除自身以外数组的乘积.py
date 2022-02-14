'''
不让用 除法，tc = O(n)
进阶：sc=O(1)。但输出数组不算额外空间。不会写。官方利用了输出数组作为向右的结果。啊这。。。
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0]*length

        # answer[i] 表示索引 i 左侧所有元素的乘积
        # 因为索引为 '0' 的元素左侧没有元素， 所以 answer[0] = 1
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]

        # R 为右侧所有元素的乘积
        # 刚开始右边没有元素，所以 R = 1
        R = 1;
        for i in reversed(range(length)):
            # 对于索引 i，左边的乘积为 answer[i]，右边的乘积为 R
            answer[i] = answer[i] * R
            # R 需要包含右边所有的乘积，所以计算下一个结果时需要将当前值乘到 R 上
            R *= nums[i]

        return answer
'''
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numslen = len(nums)
        ret = [None]*numslen
        toright = [nums[0]]*numslen
        toleft = [nums[-1]]*numslen
        for i in range(1, numslen-1):
            toright[i] = toright[i-1] * nums[i]
        for i in range(numslen-2, 0, -1):
            toleft[i] = toleft[i+1] * nums[i]
        ret[0], ret[-1] = toleft[1], toright[-2]
        for i in range(1, numslen-1):
            ret[i] = toright[i-1] * toleft[i+1]
        return ret
        # print(toleft,'\n',toright)

print(Solution().productExceptSelf([2,6]))