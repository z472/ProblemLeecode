'''
又没分析出来，oh no.还得努力思考啊。官方最优方法是DP，编码的话就一个细节需要注意，就是同一时间可能有多个值是
一样的也是最小的，那时候指针就要后移，这样结果就没有重复了。  596个测试用例，用时180ms。看到有批人很聪明的这么写。
快非常多40ms就完成了596个用例。空间换时间。
class Ugly:
    def __init__(self):
        self.nums = nums = [1, ]
        i2 = i3 = i5 = 0

        for i in range(1, 1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)

            if ugly == nums[i2] * 2:
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1

class Solution:
    u = Ugly()
    def nthUglyNumber(self, n):
        return self.u.nums[n - 1]
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dplist = [1] * (n + 1)
        p2, p3, p5 = 1, 1, 1
        for i in range(2, n + 1):
            a = min(dplist[p2] * 2, dplist[p3] * 3, dplist[p5] * 5)
            dplist[i] = a
            if a == dplist[p2] * 2:
                p2 += 1
            if a == dplist[p3] * 3:
                p3 += 1
            if a == dplist[p5] * 5:
                p5 += 1

        return dplist[-1]


mt = [10, ]
for i in mt:
    Solution().nthUglyNumber(i)
