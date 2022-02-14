'''
力扣没有Pyhton版官方题解，不过都是二分法，想学学具体编码，然后就是注意细节
'''
class Solution:
    def searchRange(self, nums, target):        # target: int, nums: list[int], return: list[int]
        if len(nums) == 0:
            return [-1, -1]
        l, r = 0, len(nums)-1
        mid = nums[(r+l+1)//2]
        while l <= r and mid != target:
            if mid > target:
                r = (r+l+1)//2-1
            else:
                l = (r+l+1)//2+1
            if 0 <= (r+l+1)//2 <= len(nums)-1:
                mid = nums[(r+l+1)//2]
            else:
                return [-1, -1]
        sep = (r + l + 1) // 2
        print('l=',l,' r=',r, ' sep=',sep)
        if l > r:
            return [-1, -1]
        elif l == r:
            return [l, r]
        outl, r1 = l, sep
        if nums[outl] != target:
            # outl, r1 = l, sep
            while nums[outl+1] != target:
                mid = (r1+outl+1)//2
                if nums[mid] < target:
                    outl = mid
                else:
                    r1 = mid
            outl = outl+1
        l1, outr = sep, r
        if nums[outr] != target:
            # l1, outr = sep, r
            while nums[outr-1] != target:
                mid = (outr+l1+1)//2
                if nums[mid] > target:
                    outr = mid
                else:
                    l1 = mid
            outr = outr-1
        return [outl, outr]

a = Solution()
test = [([5,7,7,8,8,10], 8), ([5,7,7,8,8,10], 6), ([], 0), ([-1,1,1,1,1,4], 1),]
ques = [([-1,1,1,1,1,4], -1), ([-1,1,1,1,1,4], 4), ([-1,-1,1,1,1,1,4,4], -1), ([-1,-1,-1,1,1,2,3,3,3,4,4], 1)]
lee_test = [([2,2], 3)]
for i in ques:
    print(i[0], i[1])
    print(a.searchRange(i[0], i[1]) )