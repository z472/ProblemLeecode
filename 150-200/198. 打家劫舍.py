'''
执行用时：28 ms, 在所有 Python3 提交中击败了98.61%的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了98.64%的用户
绝对是我动态规划的一个里程碑，虽然代码不复杂，但是这是我第一个 灵巧DP（自己构造概念和甚至需要构建某种结构） 类的题。
之前灵巧DP是看题解学习它的DP思想--自己解不出来，要不就是蛮力DP(爬楼梯、杨辉三角、寻路那几个)--自己解出来但有点没劲。
官方题解：就是我的算法。而且我是一步到位了，就是它改良过的最优解。
'''
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        noadd, add = 0, 0
        for i in nums:
            add, noadd = noadd+i, max(add, noadd)
        return max(add, noadd)

mt = [[1], [1,4,2]]
bug = [[4,1,2,3]]
for i in mt+bug:
    print('in:', i)
    print(Solution().rob(i))