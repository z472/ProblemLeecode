'''
执行用时：2472 ms, 在所有 Python3 提交中击败了11.19%的用户
内存消耗：25.9 MB, 在所有 Python3 提交中击败了76.12%的用户
我第一时间反应是埃及筛，但我居然觉得要sc=O(n)不好。就看官方题解埃及筛法，我觉得比较优化的细节是当一个因子为x它的子循环
就是不考虑x-1的因数了，直接从x平方算起。这个很好。
下面是400ms左右的代码。可以看出python的循环 for 要比 while 快多少。
class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [1]*n
        count = 0
        for i in range(2,n):
            if prime[i] == 1:
                count += 1
                for j in range(i*i,n,i):
                    prime[j] = 0
        return count

100ms左右的埃及筛代码。快的核心部分就是只用了一个 for 子循环的 for 被列表的切片和py 解包Unpacking 的赋值语法给实现了。
大循环的for就是你觉得用for实现不了求开方。我没动脑筋。

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0   # 0和1不是质数，先排除掉

        # 埃式筛，把不大于根号 n 的所有质数的倍数剔除
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

        return sum(isPrime)
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        ret = n - 2
        i = 2
        sav = [0] * n   # 这里就是不管0索引，只考虑1到n-1索引
        while i ** 2 <= n:
            x = i
            index = x ** 2
            while index <= n - 1:
                if sav[index] == 0:
                    sav[index] = 1
                    ret -= 1
                x += 1
                index = i * x
            i += 1
        if ret < 0:
            return 0
        return ret


mt = [10, 0, 1, 2, 3]
for i in mt:
    print(i, ':', Solution().countPrimes(i))
