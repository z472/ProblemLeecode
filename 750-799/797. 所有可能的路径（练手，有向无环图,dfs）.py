'''
不是很理解官方题解的dfs说的tc=O(n*2^n)，怎么就有2^n个路径呢？
'''
from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        def dfs(i):
            t = []
            for j in graph[i]:
                if j == n-1:
                    t += [[j],]
                else:
                    t += [[j]+i for i in dfs(j)]
            return t
        return [[0]+i for i in dfs(0)]