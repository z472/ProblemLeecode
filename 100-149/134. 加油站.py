'''
执行用时：2244 ms, 在所有 Python3 提交中击败了31.51%的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了11.10%的用户
毫无优化的一次过，但是这个用时，这么离谱吗。
官方题解数学分析都能理解，就是最后的文字推理很迷惑。试图去应用他推出的那个式子，z在x,y之间。然后从z
开始无法到达y的下一个结点是满足从z到y的=累计gas < 累计的消耗。
'''
from typing import List
from operator import sub


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        le = len(gas)
        impact = list(map(sub, gas, cost))
        for i in range(le):
            sav = impact[i]
            j = (i + 1) % le
            while sav >= 0 and j != i:
                sav += impact[j]
                j = (j + 1) % le
            if sav >= 0:
                return i
        return -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(Solution().canCompleteCircuit(gas, cost))
