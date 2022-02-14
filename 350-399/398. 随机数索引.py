'''
执行用时：128 ms, 在所有 Python3 提交中击败了73.98%的用户
内存消耗：18.2 MB, 在所有 Python3 提交中击败了96.39%的用户

纯是理解蓄水池算法和练习编码。编码也没啥可练习的。主要是理解蓄水池算法花了很久。
https://leetcode-cn.com/problems/random-pick-index/solution/zhong-gui-zhong-ju-xu-shui-chi-chou-yang-random-re/
这个题解结合自己举几个简单的数去体会就能理解。其实就是一个计算式：1/(n-1) * (n-1)/n。没有遇到所有目标值就会返回当前遇到过的平均概率。
但是这个概率对后面没有任何影响，只是因为它当前可能是最后一个目标值（那样就是对的）。只有最后一次遇到目标值的结果才是对的。
'''
from random import randint
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        times, idx = 1, 0
        reservoir = []
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                if randint(1, times) == 1:
                    idx = i
                else:
                    idx = reservoir[randint(1, times - 1) - 1]
                reservoir.append(i)
                times += 1
        return idx

mt = [3,3,3,2,1]
t = Solution(mt)
sav = []
for i in range(1000):
    sav.append(t.pick(3))
x, y, z = 0, 0, 0
for i in sav:
    if i == 0:
        x += 1
    elif i == 1:
        y += 1
    else:
        z += 1
print(x,y,z)