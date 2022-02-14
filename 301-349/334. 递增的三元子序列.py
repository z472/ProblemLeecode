'''
执行用时：36 ms, 在所有 Python3 提交中击败了  91.50%  的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了10.38%的用户
无官方题解。dp中等题。dp特点就是在 不影响当前dp结构的逻辑的情况下 把自己好的特性留下。
如果是用一个长度为k的单调栈来存储就可以判断 k 元子序列了。我这么写还是拓展性不高。
'''
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        fir = 0
        sec = 0
        lennums = len(nums)
        for i in range(lennums):
            if nums[i] <= nums[fir]:
                fir = i
            elif sec == 0:
                sec = i
            elif nums[i] <= nums[sec]:
                sec = i
            else:
                return True
        return False

mt = [[1,2,3,4,5], [2,1,5,0,4,6]]
bug = [[1,2,1,2,1,2,1,2,1,2],]
for i in mt+bug:
    print(i,'-> ', Solution().increasingTriplet(i))

'''
老版本，fir,sec初始化在第一个循环里。
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        fir = 0
        sec = 0
        lennums = len(nums)
        for i in range(lennums):
            if nums[i] > nums[fir]:
                sec = i
                break
            fir = i
        for i in range(sec, lennums):
            if nums[i] > nums[sec]:
                return True
            if nums[i] <= nums[fir]:    # bug
                fir = i
            elif nums[i] < nums[sec]:
                sec = i
        return False
'''