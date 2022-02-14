'''
这个中等题很tm不简单，题解的状态压缩有点看不懂，主要涉及的是数学的排列。这放到
高中排列组合那里就能解，编程纯纯是工具人。下面想的太简单了，有错误。
'''
class Solution:
    def countArrangement(self, n: int) -> int:
        # dp = [0 for _ in range(n+1)]
        lastnums = 1
        cal = lambda i:[i%x for x in range(1, i)].count(0)
        for i in range(2, n+1):
            lastnums += cal(i)*lastnums
        return lastnums

t = [2,3,4 ,8, 9]
for i in t:
    print(i, '--->', Solution().countArrangement(i))
