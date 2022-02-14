'''
有的题解说这个是 多重背包问题 。不管是什么问题，关键是你的分析。这题的入口很少，就一两条思路可以入手。
常见的是DP，另一个更好的是BFS（广度优先遍历）。准确说是，限制遍历深度的广度优先遍历。代码比文字的题解要好懂。
当然也是走一遍代码的逻辑，才能理解的。
class Solution:
    def numSquares(self, n):

        def is_divided_by(n, count):
            """
                return: true if "n" can be decomposed into "count" number of perfect square numbers.
                e.g. n=12, count=3:  true.
                     n=12, count=2:  false
            """
            if count == 1:
                return n in square_nums

            for k in square_nums:
                if is_divided_by(n - k, count - 1):
                    return True
            return False

        square_nums = set([i * i for i in range(1, int(n**0.5)+1)])

        for count in range(1, n+1):
            if is_divided_by(n, count):
                return count
差一些的是DP，就是把你算法进一步优化一下。但是人家变快了，也是用的迭代来写的。不过它dp就是小的值+1得到后面的。
'''
class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a = int(n**0.5)
        if a**2 == n:
            return 1
        min_ = n
        # 下面是你的无理论依据的猜测，我最初这里是1，但我觉得这样会重复计算。减掉大的数会缩小问题范围，使递归更快。
        # 但遇到了 192 这个输入，我的结果是4， 但正确值是3。
        bug = int((n//2)**0.5)
        for i in range(bug, a+1):
            min_ = min(min_, self.numSquares(n-i**2))
        return 1 + min_

def printtwo(n):
    print(int((n//2)**0.5), '\t', int(n**0.5)+1)

# for i in range(1, 19):
#     print(i, end='->')
#     printtwo(i)
mt = [3, 4, 8, 9, 17]
bug = [12, 42, 10001]
bugs = [192]
for i in mt+bugs:
    print(i, '->', Solution().numSquares(i))
