'''
执行用时：892 ms, 在所有 Python3 提交中击败了12.60%的用户
内存消耗：29.8 MB, 在所有 Python3 提交中击败了26.15%的用户
用最好的方法，写最拉的代码。下面是击败99.7%, 304ms同为双端队列的代码，学着点。

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 双端队列
        d = collections.deque()
        # 初始化窗口
        for val in nums[:k]:
            while d and d[-1] < val: d.pop()
            d.append(val)
        res = [d[0]]
        # 滑动窗口
        for idx,num in enumerate(nums[k:]):
            if nums[idx] == d[0]: d.popleft()
            while d and d[-1] < num: d.pop()
            d.append(num)
            res.append(d[0])
        return res
一.双端队列的判空可以和列表一样，while d。很简洁。
二.它滑动窗口的去除 deque的左边，每次只判断了最左边（队列最大值）是否是窗口要丢弃的那个位置。
操作最少化。你去除左边的步骤明显的乱。而且用了索引来存储，判断的。问题直接复杂化了。它比我快了66%。
'''
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        kdeque = deque([(nums[0], 0), ])
        ret = []
        numslen, kdequelen = len(nums), len(kdeque)
        for i in range(0, numslen):
            for _ in range(kdequelen):
                if kdequelen > 0 and kdeque[0][1] < i-k+1:
                    kdeque.popleft()
                    kdequelen -= 1
                elif kdequelen > 0 and nums[i] > kdeque[-1][0]:
                    kdeque.pop()
                    kdequelen -= 1
                else:
                    break
            kdeque.append((nums[i], i))
            kdequelen += 1
            ret.append(kdeque[0][0])

        return ret[(k-1):]


mt = [1, 3, -1, -3, 5, 9, 6, 7]
bug = [1,-1]
print(Solution().maxSlidingWindow(bug, 2))
for i in [1,2,3]:
    print('\t', mt)
    print(i,':',Solution().maxSlidingWindow(mt, i))
