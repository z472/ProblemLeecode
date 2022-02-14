'''
摩尔投票法的变形题。它是求大于 n//3 的众数。

学习了摩尔投票法，让人印象深刻的是它  对抗抵消  的思想，但别忘了，它还有最后的  检测  步骤。
'''
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a, b, count_a, count_b = 0, 0, 0, 0 # 设定1号众数和2号众数
        res = []

        for i in nums:
            if a == i:
                count_a += 1
                continue
            if b == i:
                count_b += 1
                continue
            if count_a == 0:
                a = i
                count_a = 1
                continue
            if count_b == 0:
                b = i
                count_b = 1
                continue
            count_a -= 1
            count_b -= 1

        count_a, count_b = 0, 0
        for j in nums:
            if j == a:
                count_a += 1
            elif j == b:
                count_b += 1
        if count_a > len(nums)/3:
            res.append(a)
        if count_b > len(nums)/3:
            res.append(b)
        return res
