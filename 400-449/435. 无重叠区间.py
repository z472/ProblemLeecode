'''
这题的难度集中在思路上。要能看出些深层的东西。

贪心算法。这题是要数量尽可能多的非重叠区间。故只要是最左区间的右端点尽可能的小，那么对于后面
的数据来说就是最好的。如果是多个右端点相同但重叠的区间就只算一个，重要的是右端点。显然，这么
操作下来，整个的问题域会减少一个。逐渐就能取得最后的答案了。对了，问题域是最少会减少一个，它
里面如果有数据的左端点比当前的最左区间的右端点还要小，这样的数据也会被删除掉。

这个逻辑是比较。。。简单，但是理解上来有点会质疑它的正确性。不过确实ok。
'''
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        pass

