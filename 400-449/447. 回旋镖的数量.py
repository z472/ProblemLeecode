'''
执行用时：844 ms, 在所有 Python3 提交中击败了88.73%的用户
内存消耗：27.9 MB, 在所有 Python3 提交中击败了9.16%的用户

刷题最妙的感觉之一就是自己没怎么测试的代码，执行一次过的感觉。
这题我是蛮力法，tc和sc都说 O(n^2) 。看力扣网友的py3提交也
差不多一个路子。有一个也是defaultdict，几乎一样。
'''
from typing import List
from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        lenpoints = len(points)
        srypoints = [defaultdict(int) for _ in range(lenpoints)]
        def calculate_i(Cdict):
            res_i = 0
            for val in Cdict.values():
                res_i += val*(val-1)
            return res_i
        res = 0
        distance = lambda i,j : (i[0]-j[0])**2+(i[1]-j[1])**2
        for i in range(lenpoints):
            for j in range(i+1, lenpoints):
                dis = distance(points[i], points[j])
                srypoints[i][dis] += 1
                srypoints[j][dis] += 1
        for i in srypoints:
            res += calculate_i(i)
        return res


t1 = [[0,0],[1,0],[2,0]]
print(Solution().numberOfBoomerangs(t1))



