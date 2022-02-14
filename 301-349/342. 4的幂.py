'''
有约束的简单题，不要用循环和递归来写。我的代码48ms。分别击败了26%,12%。
下面的28ms。tc击败99。3%

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<0 or (n & (n-1)):
            return False
        return not ((n & 0x55555555)==0)

因为题目说了 -2^31 < n < 2^31-1。故它来个穿插取交集为0的16进制。
'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n != 0 and ((n&(n-1)) == 0 == ((len(bin(n))-3) % 2))

mt = [4, 6, 8, 4**4]
for i in mt:
    print(i, Solution().isPowerOfFour(i))

print(len(bin(16)), 6%2, 16%2)