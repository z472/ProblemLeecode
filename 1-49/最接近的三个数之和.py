'''
这题最大的问题就是没有深思熟虑的改逻辑是很危险的事情。
你认为的正确可能在编程者这边持续很久但都是泡影。
'''
class Solution:
    def threeSumClosest(self, nums, target):
        le, dif = len(nums), 0
        nums.sort()
        output = nums[0]+nums[1]+nums[le-1]
        for idx, i in enumerate(nums[:-2]):
            left, right = idx+1, le-1
            sum3 = i+nums[left]+nums[right]
            if idx == 0 or i != nums[idx-1]:
                # print(i, ': ')
                while right-left>1:
                    dif = sum3-target
                    if dif==0:
                        return target
                    elif dif<0:
                        left += 1
                    else:
                        right -= 1
                    sum3 = i+nums[left]+nums[right]
                    # print(sum3, end=' ')
                    output = sum3 if abs(sum3-target)<abs(output-target) else output
                output = sum3 if abs(sum3 - target) < abs(output - target) else output
                # print('----', '\n', 'output:', output)
        return output

a = Solution()
test = [([-1, 2, 1, -4], 1), ([0, 0, 0], 1), ([0, 1, 2], 3), ([1, 2, 4, 8, 16, 32, 64, 128], 82), ([1,6,9,14,16,70],81)]
for i in test:
    print(a.threeSumClosest(i[0], i[1]))