'''
执行用时：56 ms, 在所有 Python3 提交中击败了78.51%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了74.34%的用户
也可以用堆，优先队列什么的。保存有序的结构。那样就不用像我一样遍历队列来获取可能的最小值。

我的s队列保存的二元组是nums1的索引，它的另一个值是nums2的索引，是下一个可能的取值。

它就是贪心和蛮力法的一种改良，也有点广度优先。下面是利用堆的，100%提交28ms~32ms。

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # pro
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs

代码很短，好理解，就是奇怪它的heapq是以item[0]为比较的键吗，好像是自动就完成比较了。自己测试了一下
确实是这样的，如果堆的元素是List[int]它会按该列表的首位值作为比较键。
'''
from typing import List
from collections import deque

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        s = deque()
        ret = [[nums1[0], nums2[0]]]
        s.append([0, 1])
        l1, l2 = len(nums1), len(nums2)
        while s and k-1:
            if s[-1][1] != 0 and s[-1][0] < l1-1:
                s.append([s[-1][0]+1, 0])
            if s[0][1] == l2:
                s.popleft()
            minnium, minidx = nums1[-1]+nums2[-1], 0
            for idx, i in enumerate(s):
                if minnium > nums1[i[0]]+nums2[i[1]]:
                    minidx = idx
                    minnium = nums1[i[0]]+nums2[i[1]]
            n1, n2 = s[minidx]
            ret.append([nums1[n1], nums2[n2]])
            s[minidx][1] += 1
            k -= 1
            if s[0][1] == l2:
                s.popleft()
        return ret


mt = [[1,3,5,6], [0,2,2,5]]
bug = [[1,2], [3]]
for i in [mt,bug][:]:
    print(i)
    print(Solution().kSmallestPairs(i[0], i[1], 16))


'''
蛮力法，tc=496ms > 11%, 内存占用达到了恐怖的47MB。
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        lenmn = len(nums1) * len(nums2)
        s = [0] * lenmn
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                s[i * len(nums2) + j] = [nums1[i], nums2[j]]    # bug
        s.sort(key=lambda x: x[0] + x[1])
        return s[:k]
'''