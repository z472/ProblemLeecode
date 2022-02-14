'''
这题是真的狗，算法不难分析，就是每一行数的是由上一行数+上一行数的取反组成。
官方题解的两种递归实现，是和我算法比较接近的。下面算法不知为何在k = 1,2时
会出错。很烦。     我的算法基于当前的k位置可以计算它对应的前一半的位置k-t，
最后k会变为1，就是0，这个过程中变换一次就是取反一次。
'''
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        t = 2**(n-1)
        i = 0   # 变换位置次数
        for _ in range(n-1):
            if k == 1 or t == 0:
                break
            if t == k:
                return (n-1)%2
            elif t < k:
                k -= t
                i += 1
            t //= 2
        return (i%2) ^ 0

test = [(4,5),(5, 10)]
wrong = [(2,1),(3,2)]
for i in test+wrong:
    print(Solution().kthGrammar(*i))