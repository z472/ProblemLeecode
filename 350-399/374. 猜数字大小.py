'''
二分法智商检测？？？
执行用时：32 ms, 在所有 Python3 提交中击败了94.83%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了26.35%的用户
一次通过智商检测
'''
num = 10
def guess(n):
    return 1 if n > num else (0 if n == num else -1)

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l < r:    # bug n次取不取等
            mid = (l+r)//2
            if guess(mid) == 0:
                return mid
            if guess(mid) < 0:
                r = mid
            else:
                l = mid+1
        return l

mt = [11,100,10]
for i in mt:
    print(Solution().guessNumber(i))