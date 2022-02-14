'''
执行用时：56 ms, 在所有 Python3 提交中击败了92.48%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了8.94%的用户
上面运行表现和我无关，我一个像样的算法也没想出。自己根据题意分析出一堆理论，虽然正确但有点无用。
强烈去看官方题解。那里有两种成熟的方法。
1.DP时间为O(n^2)很好，看到它设的dp结点，我也推出了递推式，推导难度不大。难在创建这个dp结点的含义这个逻辑上。索引的巨大威力。之前也
体会了一次。
2.官方说是贪心+二分。其实和二分关系不大，还是由一个贪心思路和索引展开的dp过程。tc = O(nlog(n))由于二分法的使用。它创建dp的逻辑是
设 dp[i]为长度为i的末尾的最小值。 然后还有一个论证改 dp 列表是递增的，所以可以用二分法来搜索。该结构的维护不难，在理解了那个逻辑之后。
它的dp逻辑有点像是每次都把该结点的好的影响给留下去。

谈一点收获：1.debug调试百度了下，设置断点runover next cursor跑下一个断点。除了调试器反应有点慢，几个值显示都很清楚。
2.谈谈dp算法的核心问题。这题的可操作性很强，很多地方是可以入手的。但之后容易不知方向。只能形成碎片化的逻辑。
    dp入手点，常常看到设置list[i]，然后用i来拓展成一个成熟的逻辑。说明dp需要保存一种数据结构，然后该结构的索引或是某些结构化的
东西是作为成熟算法逻辑的起始点。它只是成熟逻辑的一个组成部分，但是是必要的起始点。可以提供一点思考的方向。
    dp成功解题的逻辑往往是 创造力+想象力 的产物。一条路是尝试。更好的路径是紧密结合题意。
'''
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sav = [nums[0]] * (len(nums) + 1)
        savlen = 2  # 故意大一点
        left, right = 1, savlen
        for i in nums:
            while left < right:
                mid = (left + right) // 2
                if i <= sav[mid]:
                    right = mid
                else:
                    left = mid + 1
            sav[left] = i
            if left == savlen:
                savlen += 1
            right = savlen  # bug
            left = 1
        return savlen - 1

bug = [9,3]
mt = [[10,9,2,5,3,7,101,18], bug]
for i in mt:
    print(i, '->', Solution().lengthOfLIS(i))


