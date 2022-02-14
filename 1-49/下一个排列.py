class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == sorted(nums, reverse=True):
            nums.sort()
            print(nums)
            return
        if nums[-2] < nums[-1]:
            nums[-1], nums[-2] = nums[-2], nums[-1]
            print(nums)
            return
        else:
            for i in range(1, len(nums)):
                if nums[-i] > nums[-i-1]:
                    a = -i
                    while a < 0 and nums[-i-1] < nums[a]:
                        a += 1
                    nums[-i-1], nums[a-1] = nums[a-1], nums[-i-1]
                    nums[-i:] = sorted(nums[-i:])
                    print(nums)
                    return


a = Solution()
test = [[1, 3, 4, 2, 4, 4, 4], [3, 4, 5, 3, -2, -4], [9, 5, 4, 3, 1], [2, 3, 4, 6, 6, 4], [2], [1, 3], [1, 3, 2]]
for i in test[:]:
    a.nextPermutation(i)