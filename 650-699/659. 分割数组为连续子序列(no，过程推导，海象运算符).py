'''
这题目没想出一点头绪（主要是游戏让我变傻:=），我一直纠结在遍历到列表开头的元素的处理。
这是一个特殊情况，看官方题解一的方法没那么困难，从普通的元素位置（有前置元素）的角度展开
分析，自然的将特殊情况归入到一般情况中（如果我想到那里也是一样）。当然这题解似乎避开了
重复值这一点，我想的时候总会被它困住。     题解一的算法过程比较长了，这个类型概括为推理描述型
算法。利用哈希表和最小堆（py的heapq默认为最小堆，官方说是为了方便原地排序构造）就可以很好的解决

对了，我对该算法的疑问是源头性的，为何这么做是对的？（一般情况：当前遍历x值，对x-1最短长度去加一）
为何这个操作是对的？

因为题目的一个用例  [1,2,3,3,4,4,5,5]，这里的如果改成  [1,2,3,3,3,4,4,5,5]。遍历到3该
如何选择呢？  该问题有两方面的限制：连续数，最小长度>=3。常规的思路就是先取出数让它们连续，然后贪心
的让长度条件符合。所以它的正确性应该是（抽象）算法行为赋予的。

下面看下题解的py3代码，有个很有趣的点。注意那个3.8新的特性：海象运算符 :=
'''
import collections
import heapq
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        mp = collections.defaultdict(list)
        for x in nums:
            if queue := mp.get(x - 1):
                prevLength = heapq.heappop(queue)
                heapq.heappush(mp[x], prevLength + 1)
            else:
                heapq.heappush(mp[x], 1)

        return not any(queue and queue[0] < 3 for queue in mp.values())
