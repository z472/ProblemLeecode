'''
执行用时：68 ms, 在所有 Python3 提交中击败了15.12%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了18.70%的用户
二分法就这？一次过，但是看到这表现已经崩溃。
官方题解：数学转化，不用开平方，就转化为x**(1/2) -->
e**(ln(x)*(1/2))但是说是浮点数计算有误差也可能为x+1

补充知识：math.exp(x)
返回e次x幂，其中 e = 2.718281... 是自然对数的基数。
这通常比math.e**x或pow(math.e, x) 更精确。
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans
(力扣已经引入math了，自己测得手动调用)
方法二：二分法查找，但它是直接从0到x中开始二分，我是根据x的位数计算出平方根的合理位数，
在位数符合解的位数范围内开始二分的。讽刺的是，那个上去就二分的提交结果是
    执行用时：44 ms, 在所有 Python3 提交中击败了75.44%的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了20.40%的用户
比我这个改良版的快很多（我是68ms）。我tm就是个小丑。在71那题我也是改良个栈的算法，
把出栈用赋值替换，然后找标记值等等，写了一堆。然后比一个用各种内置函数O(n)复杂度的
要慢，50%和90%的差距，我再也不“改良”了，直接莽写吧，思路一样想尽量少利用内置函数
结果是既麻烦了自己速度还慢于别人。（也可能是py3内置函数的部分优化不错，比如最近了解
到它的平方就是用新学的那个快速幂的算法来实现的，包括之前也了解到它的排序算法，也是
快速排序等等复杂度很低的好算法来实现的）
方法三：牛顿迭代
牛顿迭代法是一种可以用来快速求解函数零点的方法。详见
https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/
'''
class Solution:
    def mySqrt(self, x):
        # x: int) -> int:
        n = (len(str(x))+1)//2
        if x == 0:
            return 0
        i, j = int('1'+'0'*(n-1)), int('9'*n)
        if j**2 == x:
            return j
        mid = (i+j)//2
        while j - i > 1:
            a = mid**2
            if a == x:
                return mid
            if a > x:
                j = mid
            else:
                i = mid
            mid = (i+j) // 2
        return i

a = Solution()
mt = [10**2, 99**2, 100**2, 999**2, 9999999**2, 5, 0]
for i in mt:
    print('in:', i)
    b = a.mySqrt(i)
    print(b, b**2, (b+1)**2)