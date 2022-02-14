'''
执行用时：40 ms, 在所有 Python3 提交中击败了87.18%的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了6.18%的用户
代码依旧丑陋，我这循环判断像个猪头，思路没多大区别，主要是写法：
多变量，然后清晰了很多，读代码也清晰很多，增加一个place表判断的
也增加了清晰程度，有点无聊呀这东西
class Solution:
    def insert(self, intervals, newInterval):
        left, right = newInterval
        placed = False
        ans = list()
        for li, ri in intervals:
            if li > right:
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                ans.append([li, ri])
            else:
                left = min(left, li)
                right = max(right, ri)
        if not placed:
            ans.append([left, right])
        return ans
'''

class Solution:
    def insert(self, intervals, newInterval):
        # intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in intervals:
            if i[1] >= newInterval[0]:
                if not res or res[-1][1] != '-1':
                    res.append([min(i[0], newInterval[0]), '-1'])
            else:
                res.append(i)
            if i[1] >= newInterval[1]:
                if i[0] > newInterval[1]:
                    res[-1][1] = newInterval[1]
                    res.append(i)
                else:
                    res[-1][1] = i[1]
                res += intervals[intervals.index(i) + 1:]
                return res
        if intervals[-1][1] < newInterval[1]:
            if res[-1][1] == '-1':
                res[-1][1] = newInterval[1]
            else:
                res.append(newInterval)
        return res


a = Solution()
mytest = (
    [[1, 3], [5, 5]], [3, 5], [[-4, -2], [1, 3], [6, 9]], [-12, 15], [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
    [4, 7])
for i in range(len(mytest) // 2):
    print('in:', mytest[i * 2], ' | ', mytest[2 * i + 1])
    print(a.insert(mytest[i * 2], mytest[i * 2 + 1]))
