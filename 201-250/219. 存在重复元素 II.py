from typing import List
'''
这是网友的题解，先看的官方题解，里面介绍了几个超时的数据结构，还是要用哈希表来处理。但它的写法和官方的哈希方法
差了一个删除旧的结点这个。这地方感觉可以用一个k大小的队列来类似栈的方式记录更新旧的结点。
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 创建哈希表
        hash_map = {}
        # 遍历一次数组
        for idx, n in enumerate(nums):
            if n not in hash_map or (idx - hash_map[n]) > k:
                hash_map[n] = idx
            else:
                return True
        else:
            return False