'''
执行用时：36 ms, 在所有 Python3 提交中击败了52.94%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了61.18%的用户
通过测试用例：77 / 77

说是吃豆人游戏，但从题目找到的信息发现，只是比玩家和阻碍者谁能先到终点。因为阻碍者可以先到终点，然后不动，
玩家永远也不会逃脱。它有“不动”这操作，问题就变味了。
'''
from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        a = abs(target[0]) + abs(target[1])
        for i in ghosts:
            if abs(i[0] - target[0]) + abs(i[1] - target[1]) <= a:
                return False
        return True
