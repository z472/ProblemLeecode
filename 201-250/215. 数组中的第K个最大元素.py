'''
里面有一个仿照快速排序的寻找无序列表中第k位元素的方法。在后面也有用到324.摆动排序II中。
'''
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass


mt = [1, 1, 2, 2, 3, 4, 5, 5, 6, 6]
for i in range(1, 7):
    print(i, '-', Solution().findKthLargest(mt, i))
bug = [3,2,3,1,2,4,5,5,6]
print(Solution().findKthLargest(bug, 4))
