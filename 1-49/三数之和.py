class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        last = nums[0] - 1
        output = []
        for idx, i in enumerate(nums[:-2]):
            if i != last:
                left, right = idx + 1, len(nums) - 1
                last2 = nums[left] - 1
                while left < right:
                    sum3 = i + nums[left] + nums[right]
                    if nums[left] == last2:
                        left += 1
                    elif sum3 == 0:
                        output.append([i, nums[left], nums[right]])
                        last2 = nums[left]
                        left += 1
                    elif sum3 < 0:
                        last2 = nums[left]
                        left += 1
                    else:
                        right -= 1
                last = i
        return output

a = Solution()
test = ([-1, 0, 1, -1, -4, 2], [-2, 9, -7],[0,0,0,0,0])
for i in test:
    print(a.threeSum(i))
