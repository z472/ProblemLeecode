'''
要找出找全所有的交叉情况，分类标准是边的数目，4条边何时交叉，5条，6条。一共三种。
看似不难，找全找对它们很难。
'''
from typing import List


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        return False