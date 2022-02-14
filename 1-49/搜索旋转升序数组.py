class Solution:
    def search(self, nums, target):   #nums:list[int]  target:int
        n, tag = len(nums), 0
        if n == 0:
            return -1
        mid = nums[n//2]
        # print(mid)
        if mid == target:
            return n // 2
        elif nums[-1] < nums[0]:
            if mid > nums[0]:
                if target > mid:      # target > mid and mid < nums[n//2+1]
                    tag = 1
                elif target < mid and target <= nums[-1]:
                    tag = 1
            else:
                if nums[-1] >= target > mid:
                    tag = 1
        else:
            if mid < target:
                tag = 1
        if tag == 1:
            if self.search(nums[n//2+1:], target) == -1:
                return -1
            else:
                return self.search(nums[n//2+1:], target) + n//2 + 1
        else:
            if self.search(nums[:n//2], target) == -1:
                return -1
            else:
                return self.search(nums[:n//2], target)
'''
力扣官方非递归的写法：我的切片的话占空间更大些
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
'''

a = Solution()
test = [([4,5,6,7,0,1,2], 0), ([0,1,2], 0), ([0], 0), ([4,5,6,7,0,1,2], 7), ([4,5,7,0,1,2,3], 2), ([1,2,3], 2), ([4,5,7,11,19,2,3], 3)]
lee_test = [([1], 2), ([3,5,1], 1), ([3,4,5,6,7,1,2], 4)]
for i in range(len(test)):
    print(test[i][0], '  ', test[i][1])
    print(i,':', a.search(test[i][0], test[i][1]))
    print(test[i][0].index(test[i][1]))
for i in lee_test:
    print(i[0], '  ',i[1])
    print('index:', a.search(i[0], i[1]))