'''
接雨水的道理大家都懂，就是木桶短板原理。但是并不好写。我是不会写。分析在下面。

import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) <= 2 or len(heightMap[0]) <= 2:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = set()
        heap = []
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
            visited.add((i, 0))
            visited.add((i, n-1))
        for j in range(1, n-1):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m-1][j], m-1, j))
            visited.add((0, j))
            visited.add((m-1, j))

        ans = 0
        while heap:
            h, i, j = heapq.heappop(heap)
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i, new_j = i + x, j + y
                if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in visited:
                    near_h = heightMap[new_i][new_j]
                    if near_h < h:
                        ans += h - near_h
                    heapq.heappush(heap, (max(h, near_h), new_i, new_j))
                    visited.add((new_i, new_j))
        return ans

# 作者：jue-qiang-zha-zha

这题是又会又不会的类型。想的不够全面，没联系学过的知识。
    之前一直想的是，直接遍历，不会。它的是根据桶的边缘逐渐向内遍历。还用了最小堆（优先队列）的结构。
    它们用最小堆来保留木桶的短板，先计算整个的边界。然后遍历每个位置，计算该位置的接水量，然后关键操作是
维护这个“桶”的边缘。它遍历也不能是对二维数组做直接的循环遍历，它是根据边缘，逐渐向内遍历。然后建立一个已遍历的
集合，避免重复计算存水量。

很难吗？看了一会就懂了。不难理解。想的不全面。
'''