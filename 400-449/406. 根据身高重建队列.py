'''
我15分钟解决的中等题。tc=388 ms	 sc=15.1 MB
这题我之前有标记过，是我力扣做的第一道题。历史记录显示在2020.11.17提交错了5次（后4次是超时）

思路来自，我随意的一次预处理，排序。按照从高到低排序i[0],然后在按照i[1]从低到高排序。因为它代表着
该元素前面有几个人。然后解法就呼之欲出了。但我居然用时400ms。

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        n = len(people)
        ans = list()
        for person in people:
            ans[person[1]:person[1]] = [person]
        return ans

官方的代码，和我一样的从高到低按身高，然后i[1]按从低到高。但它的写法很bug。更像开挂的是，它的速度，tc=44ms

'''
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(reverse=True, key=lambda x: (x[0], -x[1]))  # 这里不错想的
        for idx, i in enumerate(people):
            while idx != i[1]:
                people[idx], people[idx - 1] = people[idx - 1], people[idx]
                idx -= 1
        return people

mt = [[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]],]
for i in mt:
    print('input:', i)
    print(Solution().reconstructQueue(i))

