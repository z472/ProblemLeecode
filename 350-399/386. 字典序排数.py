'''
不要自己给自己加戏好吗？递归的都没写就去写迭代版本的。没有看到有题解是用迭代实现的。
最初写了一个迭代的。不符合题意。理解错了。后面又想不出来。

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        if n < 1:
            return []
        res = []

        def dfs(cur):
            if cur > n:
                return
            res.append(cur)
            for j in range(10):# 遍历0 ~ 9
                dfs(cur * 10 + j)

        for i in range(1, 10):# 遍历1 ~ 9
            dfs(i)
        return res
看了递归版本的发现你居然不想用栈，来写非递归。哦，简直离谱。
这题看了下，速度快的提交是用sort做的。这就是个nt题。
'''
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [1] * n
        fir, x, idx = 1, 1, 0
        if n < 10:
            return [i + 1 for i in range(n)]
        while idx < n:
            while x*10 <= n:
                ans[idx] = x
                idx += 1
                x *= 10

            for i in range(x, min(x+11, n+1)):
                ans[idx] = i
                idx += 1
            x += 1
            while x % 10 == 0:
                x //= 10
        return ret

mt = [34, 121]
bug = [100]
for i in mt+bug:
    print('input:', i)
    print(Solution().lexicalOrder(i))

