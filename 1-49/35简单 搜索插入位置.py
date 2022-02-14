'''
一次过的，但是为何我的空间占用这么高呢，在py3中仅仅击败了7%的人？？？
'''
class Solution:
    def searchInsert(self, nums, target):   # nums: list[int]  target: int   return : int
        l, r = 0, len(nums)-1
        while l <= r:
            mid = nums[(l + r + 1) // 2]
            if mid == target:
                return (l+r+1)//2
            elif mid < target:
                l = (l+r+1)//2 + 1
            else:
                r = (l+r+1)//2 - 1
        print('r=', r,' l=', end='')
        return l

a = Solution()
test = [([1,3,5,6], 5), ([1,3,5,6], 8), ([1,3,5,6], -5)]
for i in test:
    print(i[0], ' ',i[1])
    print(a.searchInsert(i[0], i[1]) )