'''
执行用时：56 ms, 在所有 Python3 提交中击败了36.73%的用户
内存消耗：17.9 MB, 在所有 Python3 提交中击败了36.95%的用户

秒杀题,和官方题解一样，它也只有一个思路
'''
from typing import List
from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d1 = defaultdict(int)
        curmax = 0
        for i in range(len(wall)):
            add = 0
            for j in range(len(wall[i])-1):
                add += wall[i][j]
                d1[add] += 1
                curmax = max(curmax, d1[add])
        return len(wall)-curmax
