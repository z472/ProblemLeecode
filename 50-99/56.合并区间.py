'''
    运行，空间分别是超过了95%,19%。空间占用比90%水平差了1MB，这是基于它测试用例的数量的。
所以运行快但总体表现并不很好。包括你用list.sort()对列表的预处理这一操作，很一般。
    官方题解：第一种和我一样的预处理但没有维护left和right的写法。看了它的写法产生个问题，
我为何要创建这两个变量？好吧，应该是我没看到循环带来的全部效果。
    淦，没有别的解法了。无聊的一批这。。
    class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
'''
class Solution:
    def merge(self, intervals):
        # intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        res = []
        left, right = intervals[0][0], intervals[0][1]
        for i in range(len(intervals)):
            if intervals[i][0] > right:
                res.append([left, right])
                left = intervals[i][0]
            right = max(intervals[i][1], right)
        res.append([left, right])
        return res

a = Solution()
mytest = ([[1,3],[2,6],[8,10],[15,18]], [[1,4],[2, 3],[5,9]], )
lee_test = ([[1,4], [0,3], [6, 7], [-3, 1]],)
for i in lee_test:
    print('in:', i)
    print(a.merge(i))



