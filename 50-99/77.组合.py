'''
执行用时：364 ms, 在所有 Python3 提交中击败了70.00%的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了18.00%的用户
第二次过的，第一次由于返回代码是不支持k=1的情况，就特例化了两行。出现的问题主要是child过早返回和sav忘记
切片，还有题目要求是1到n，最初写的是0到n-1的。算法就是用个sav来动态存每个测试用例，sav后面位置的数只能比
它前一位的要大。
官方题解：
'''
class Solution:
    def combine(self, n, k):
        # 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
        # n: int, k: int) -> List[List[int]]:
        res = []
        sav = [1]*k
        if k == 1:
            return [[_] for _ in range(1, n+1)]
        def child(i):
            for j in range(sav[-i]+1, n+1):
                sav[-i+1] = j
                if i == 2:
                    res.append(sav[:])
                else:
                    child(i-1)
            return
        for _ in range(1, n-k+2):
            sav[0] = _
            child(k)
        return res
a = Solution()
mt = [(4,1), (5, 3)]
for i in mt:
    print('in:', i)
    print(a.combine(i[0], i[1]))