'''
执行用时：36 ms, 在所有 Python3 提交中击败了78.44%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了23.79%的用户
一次过，但是这个题目真的是给我绕到算排列组合里去了，为何是加前一个
或是前二个呢，就是动态规划，每次都是贪心得到各自数的所有方法，该步
只能加1或是2所以分别是前一个数的所有方法数+前二步的所有方法数。
所以可以拓展爬楼梯一次爬个1，2,3,4,,,n步

官方有三种解法，我那是O(n)最基础的解法，第二种是矩阵快速幂O(logn)
把题目转化为矩阵递归的写法，然后去计算递归的矩阵，但是可惜没有py3代
码，https://leetcode-cn.com/circle/article/8uRHgu/ 这个帖
子有写普通快速幂算法和矩阵快速幂算法的py3实现代码。
def fpowx(x, n):
    res = 1
    while n:
        if n & 1:
            res = res * x
        # compute x^2 x^4 x^8
        x *= x
        n >>= 1
    return res
这是它x**n的快速幂实现，一个知识是n & 1为位运算是把正数看作是二进制形式
把它与1做“与”运算(其实就是最后一位与1做与运算)，然后>>==是右移运算符，
一般配合按位与运算符。
def fmulti(m, n, mod=10 ** 9 + 7):
    res = 0
    while n:
        if n & 1:
            res += m
        m = (m + m) % mod
        res %= mod      # 还可以这样写
        n >>= 1
    return res
这是那帖子里的--防止乘法溢出的算法，也是按位与然后右移缩小为1/2,矩阵快速幂
类似整数的快速幂，复杂度减少的地方在于幂上，那里的res初始值为单位矩阵，还要
先写一个矩阵乘法（最基本的多重循环实现），其他都类似于普通的快速幂。

总结，这个快速幂的思想就是由数的二进制形式展开这个事实，来以平方倍缩小范围的

方法三：通项公式：我看后--> 没太懂
'''
class Solution:
    def climbStairs(self, n):
        # n: int) -> int:
        '''
        题目：假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
        每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
        注意：给定 n 是一个正整数。
        '''
        if n < 3:
            return n
        pre1, pre2 = 1, 2
        for i in range(3,n):
            a = pre2
            pre2 = pre1 + pre2
            pre1 = a
            print(pre2, end=' ')
        return pre1+pre2

a = Solution()
mt = [8, 11]
for i in mt:
    print('in:', i)
    print(a.climbStairs(i))