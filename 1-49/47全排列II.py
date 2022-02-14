'''
这题运行速度击败99.38%，内存击败34%，但是我主要是根据“全排列1"官方的py3题解代码修改来的
故不完全是自己的功绩。继续努力吧。
'''
class Solution:
    def permuteUnique(self, nums):
        # nums: List[int]) -> List[List[int]]:
        def child(first=0):
            s1 = dict()
            if first == n:
                res.append(nums[:])
            else:
                for i in range(first, n):
                    if not s1.get(nums[i]):
                        nums[first], nums[i] = nums[i], nums[first]
                        child(first+1)
                        nums[first], nums[i] = nums[i], nums[first]
                        s1[nums[i]] = 1

        n = len(nums)
        res = []
        child()
        return res

a = Solution()
mytest = [[1,1,2,3,], ]
for i in mytest:
    print('in:', i)
    print(a.permuteUnique(i))