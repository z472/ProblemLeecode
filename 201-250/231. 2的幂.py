'''
40ms。下面写28ms
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        return n&n-1==0

如何获取二进制中最右边的 1：x & (-x)。
    负数的二进制是补码，即 整数的二进制取反+1.它的最后一位1和正的位置一样。其他位置都不一样。
如何将二进制中最右边的 1 设置为 0：x & (x - 1)。
    之前201题讲过的技巧，x & (x-1)会把x的最后一个1设置为0.
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return not n & n-1 if n > 0 else False

mt = [1,2,3,8]
bug = [0]
for i in mt+bug:
    print(Solution().isPowerOfTwo(i))