'''
这题最大的收获，是不起眼的地方。在left的初值上，如果设置像我一样为0.
22测试用例，耗时92ms。如果改成1，因为version是从1开始算的。耗时32ms。
直接差了3倍的速度。
'''
def isBadVersion(version):
    return True if version >= 0 else False

class Solution:
    def firstBadVersion(self, n):
        left, right = 0, n
        while left < right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        return left

mt = [7, 6]
for i in mt:
    print(Solution().firstBadVersion(i))