'''
执行用时：256 ms, 在所有 Python3 提交中击败了16.67%的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了95.56%的用户
惨胜！这题主要是在加1或是减1的时机上。下面的代码说只有两种情况下减1效果更好。
这肯定是数学上的推演。我也类似的用位运算分析过。我清楚减1是把那位置用两个操作实现成了0。还有就是
加1操作会让7,15，这样的2^n-1会更快的替换。但如果前面还有数字，比如0b1100111它加1前面会多出来一个1.
反正就是没推出来。
class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n != 1:
            if (n & 1) == 0: # 偶数直接右移
                n >>= 1
            else:
                # 奇数01或者3减一，其他加1
                if (n & 2) == 0 or n == 3:
                    n += -1
                else: n += 1
            count += 1
        return count
'''
class Solution:
    def integerReplacement(self, n: int) -> int:
        def dfs(x):
            ret = 0
            while x & 1 == 0:
                ret += 1
                x >>= 1
            if x == 1:
                return ret
            return min(dfs(x - 1), dfs(x + 1)) + ret + 1

        return dfs(n)



mt = [2, 3, 4, 5, 6, 7, 16, 65535]
for i in mt:
    print(i, Solution().integerReplacement(i))
