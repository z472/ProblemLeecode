'''
执行用时：48 ms, 在所有 Python3 提交中击败了13.74%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了19.90%的用户
第三次过的，之前错在了一个不进入子循环，一个是0位置的处理。但看到执行表现，我这个类似单调栈的写法，貌似是很糟糕的。
官方题解：
'''
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        for i in nums2:
            if m:
                for j in range(m-1, -1, -1):
                    if nums1[j] <= i:
                        nums1[j+1] = i
                        break
                    else:
                        nums1[j+1] = nums1[j]
                if j == 0 and i < nums1[1]:
                    nums1[0] = i
            else:
                nums1[0] = nums2[0]
            m += 1
        print(nums1)

a = Solution()
mt = [([1,2,3,0,0,0],[2,5,6]), ([0,0],[2,2]), ([2,0], [1]), ([0], [1])]
for i in mt[:]:
    print('in:', i[0], i[1])
    a.merge(i[0], len(i[0])-len(i[1]), i[1], len(i[1]))