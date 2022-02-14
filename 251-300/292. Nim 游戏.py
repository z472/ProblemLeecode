'''
初中数学题。
'''
class Solution:
    def canWinNim(self, n: int) -> bool:
        dp = [True]*n
        for i in range(3, n):
            for j in range(1, 4):
                if i-j >= 0 and not dp[i-j]:
                    dp[i] = True
                    break
            else:
                dp[i] = False
        print(dp)
        return dp[-1]

class Solution1:    # 写法1
    def canWinNim(self, n: int) -> bool:
        # 下面写成 return not n%4 == 0会变快。
        return True if n % 4 else False


mt = [12]
for i in mt:
    print(Solution().canWinNim(i))