'''
审题审歪了
'''
class Solution:
    def permuteUnique(self, nums):
        # nums: List[int]) -> List[List[int]]
        global n, tag           # nums不能设置为全局变量，会报错
        def back(nums, first=0):
            global n, tag     # 报错NameError: name 'n' is not defined，如果在两个地方都写会过度过去这里
            if n > 1 and tag == 0:
                nums.sort()
                last = 0
                for i in range(1, n):
                    if nums[i] != nums[last]:
                        last += 1
                        nums[last] = nums[i]
                nums = nums[:last+1]
                tag, n = 1, len(nums)
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                nums[i], nums[first] = nums[first], nums[i]
                back(nums, first + 1)
                nums[i], nums[first] = nums[first], nums[i]

        # tag, res, n = 0, [], len(nums)
        tag = 0
        res = []
        n = len(nums)
        back(nums)
        return res

a = Solution()
mt = [[1,2,1,4,2], []]
for i in mt:
    print('输入:', i)
    print('输出:', a.permuteUnique(i))