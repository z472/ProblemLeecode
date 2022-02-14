'''
纯不会，虽然这是道简单难度的题。但它的要求是tc=O(n)，且sc=O(1)。下面是官方题解的代码。
没有想到  异或  这个运算。回过头来貌似只有题目中的2个相同数字，可以称作小小的--暗示。
    确实它这个方法很 惊艳。知识范围跳出了常规的套路。虽然适合的场景可能不够多。但是特殊甚至是极端
情况往往需要这种 惊艳 的操作。
'''
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

print(1^3)
print(1^3^1)