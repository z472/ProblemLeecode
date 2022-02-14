# 你写的大白话，超时
class MyShitCodes:
    def lastRemaining(self, n: int) -> int:
        sav = [i for i in range(1, n + 1)]
        lensav = n
        for i in range(n // 2):
            if lensav == 1:
                return sav.pop()
            if i % 2 == 0:
                sav = sav[1::2]  # bug
            else:
                sav = sav[-2::-2][::-1]
            lensav //= 2


# 别人的数学映射+递归，能处理上亿的输入。这个数学映射来推导递归的表达式。有点数学归纳法的感觉。是设k归纳出来的。
# 它最核心的逻辑是用保留下来的数字来往回映射。它的每个递归都代表着当前层次的下一次保留的数字。最后结尾是长度为1.

class Solution1:
    def lastRemaining(self, n: int) -> int:
        return 1 if n == 1 else 2 * (n // 2 + 1 - self.lastRemaining(n // 2))


# 有个“勇士”写了非递归版本。它的那个从右向左切片的逻辑没找出来。n = n[flag or length & 1:: 2]
# 性能和上面差不多，因为tc差了不到10ms但总的测试有3.7k个
class Solution2:
    def lastRemaining(self, n: int) -> int:
        n = range(1, n + 1)
        flag = True

        while (length := len(n)) != 1:
            n = n[flag or length & 1:: 2]
            flag = not flag

        return n[0]


mt = [10 ** 8]
for i in mt[:1]:
    print('n=', i)
    print(Solution().lastRemaining(i))
