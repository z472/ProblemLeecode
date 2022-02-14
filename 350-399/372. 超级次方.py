'''
不会，下面是网友代码，那个求(x^n)%m函数有点快速幂的感觉。
我被提给的测试用例的范围给 吓 到了，b是一个2000位的数，wow，它还是一个幂，底数最大2^31-1。
无官方题解，看了些别人写的，宏观上的理解是把一步计算改成了分步很小的计算。基于指数幂的拆分和
巨大指数幂要用 快速幂 来解决（它的qpow函数）。


'''

'''
看不懂它的快速幂。乘除法优先级 > 位运算 > 加减法。

执行用时：108 ms, 在所有 Python3 提交中击败了74.09%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了86.44%的用户

class Solution:
    # 终于看懂了它的快速幂。先理解它从末尾逐渐减少n的值，n >>= 1这两个操作。
    # 它就是以log速度缩小的意思。如果n的末尾是0，一个循环n直接变成原来一半由于右移。x就需要平方来
    # 平衡这操作造成的后续改变。
    
    可以这么理解：
    本来要求x^n % m  如果n为偶数，(x^2)^(n//2) % m
    但这里ans变量还是不好理解。
    
    def qpow(self, x, n, m):
        ans = 1
        while n > 0:
            if n & 1 == 1:
                ans = ans * x % m
            x = x * x % m
            n >>= 1
        return ans

    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for i in b:
            # 下面基于 a^x * a^y = a^(x+y)把 a^b 给拆开了
            res = self.qpow(res, 10, 1337) * self.qpow(a, i, 1337)
        return res % 1337
'''

'''
这是递归版本的
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        base = 1337

        if not b:
            return 1
        last = b.pop()

        part1 = (a ** last) % base
        part2 = (self.superPow(a, b) ** 10) % base

        return (part1 * part2) % base

'''