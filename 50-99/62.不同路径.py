'''
执行用时：32 ms, 在所有 Python3 提交中击败了94.11%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了5.12%的用户
简单的排列组合知识，zz一样的题目
'''
class Solution:
    def uniquePaths(self, m, n):
        # m: int, n: int) -> int:
        dividend, divisor = 1, 1
        mi = n-1 if m > n else m-1
        for i in range(m+n-2, m+n-2-mi, -1):
            dividend *= i
        for i in range(mi, 0, -1):
            divisor *= i
        print(dividend, divisor)
        return dividend//divisor

a = Solution()
mytest = [(3,7), (2,2), (2,1), (1,1)]
for i in mytest:
    print('in:', i)
    print(a.uniquePaths(i[0], i[1]))
