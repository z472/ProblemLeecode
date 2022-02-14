'''
执行用时：56 ms, 在所有 Python3 提交中击败了40.72%的用户
内存消耗：17.5 MB, 在所有 Python3 提交中击败了46.31%的用户
我这个不符合题目要求的tc。因为我不知道Counter中的most_common(k)函数是什么复杂度的。
不过想要比 NlogN 小。不一定是到 N 吗。把哈希表中的值一共有k个，再把这k个值排序。题解里说是用堆 Nlogk。

它还有一个215题的 快速选择的算法。 我没看懂官方的描述。
'''
from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dc = Counter(nums)
        return [i for i, j in dc.most_common(k)]

mt = ['aaabbbbccd']
