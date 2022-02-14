'''
不会在线性时间，和常数复杂度解决的。看了官方题解，写的。
和136,137题是一类。最好的方法就是用位运算中的异或^来做。
异或支持交换律和结合律，0 ^ a = a; a ^ a = 0 即出现偶数次的元素是刚好可以变成0,0还可以继续去运算，并不
影响奇数次的元素。137那个题还没看懂。这题和136很像。但是它里面有两个出现为1次的元素。连续异或的结果是一个奇怪的
值x。算法从它入手分析的。其实也没太多分析。主要还是它这个分组的思想。把问题转化成136题了。emmmmmm。。。
'''
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for i in nums:
            x ^= i
        tag = x&(-x)
        ret1, ret2 = 0, 0
        for i in nums:
            if i & tag == tag:
                ret1 ^= i
            else:
                ret2 ^= i
        return [ret1, ret2]


mt = [1,2,1,3,2,5]
Solution().singleNumber(mt)
