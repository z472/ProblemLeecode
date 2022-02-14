'''
给定两个大小为 m 和 n 的正序（从小到大）数组nums1 和nums2。请你找出并返回这两个正序数组的中位数。
进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
'''
'''
示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000
'''
'''
以下是比较笨的方法：遍历的方式找到中位数，里面很多是判断是否越界的，low的很。官方题解是一个“奇怪“的二分“排除”法。
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2): # nums为list[int],返回值为float
        # 由于是算中位数，还是正序的输入。对于总长为奇数的，就找出那个正确位置的数即可；对于为偶数的，就找出那两个值即可。
        summ = len(nums1)+len(nums2)
        # 奇:1,2,...,summ//2+1 偶:1,2,...,summ//2,summ//2+1
        a, b, out = 0, 0, 0
        times = summ//2
        print(times)
        for i in range(0, times):       # 比价n次，得到第n+1的值
            if a == len(nums1) or b == len(nums2):     # 递增之后一个列表走到最后索引+1的值，同时也是输入为空列表时
                break
            if nums1[a] < nums2[b]:
                a += 1
            else:
                b += 1
        print('a=', a, '  b=', b)
        # 底下这样写就显得很呆，想把长度较小的改名成nums1，然后就写一半就行了，因为就算是a,b超出索引被break出来了也
        # 只有可能发生在较小的那个列表（如果是较大的列表索引一直长，它也会先到中位数就跳出，不会走到break）
        # 但很尴尬的是发现，还有长度相等的可能，那样就nums1,2都有可能是超出索引（一个列表最小的比另一个列表中最大的还大的情况）
        if a == len(nums1):
            t = times-a
            x = nums2[t]
            if summ % 2 == 0:
                if a:
                    if t != 0:
                        x += nums2[t-1] if nums1[a-1] < nums2[t-1] else nums1[a-1]
                    else:
                        x += nums1[a-1]
                else:
                    x += nums2[t-1]
                x /= 2
        elif b == len(nums2):
            t = times-b
            x = nums1[t]
            if summ % 2 == 0:
                if b:
                    if t != 0:
                        x += nums2[b-1] if nums1[t-1] < nums2[b-1] else nums1[t-1]
                    else:
                        x += nums2[b-1]
                else:
                    x += nums1[t-1]     # 复制之前，类比之前的代码来实现时。写错了。
                x /= 2
        elif a+b == times:
            x = nums2[b] if nums1[a] > nums2[b] else nums1[a]
            if summ % 2 == 0:
                if a != 0 and b != 0:
                    x += nums2[b-1] if nums1[a-1] < nums2[b-1] else nums1[a-1]
                elif a == 0:
                    x += nums2[b-1]
                elif b == 0:
                    x += nums1[a-1]
                x /= 2
        return x


a = Solution()
t_set = (([], [2, ]), ([], [1, 3, 4]), ([1, 2], [3, 6, ]), ([3, ], [1, 2, 11]))
for i in t_set:
    n1, n2 = i[0], i[1]
    print(a.findMedianSortedArrays(n1, n2))















