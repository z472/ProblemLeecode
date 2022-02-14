'''
执行用时：44 ms, 在所有 Python3 提交中击败了41.14%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了24.96%的用户
第四次才过，但是由于之前做过三道类似的题，153,81,1-49有一个。难度也不是很难。官方是部分二分法。也我写递归那里。
然后它去让rr -= 1。不是纯正的二分法。虽然可以直接min(nums)求出答案，或是用一些写法，部分二分法，不去递归来写
但是毕竟还是在简单的整数数组上去弄，真正的地方肯定是把数据复杂成某种类型，到时候就不好直接min()了。
'''
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        rl, rr = 0, len(nums)-1
        while rl < rr:
            rmid = (rl+rr)//2
            if nums[rl] >= nums[rr]:
                if nums[rmid] > nums[rr]:
                    rl = rmid + 1
                elif nums[rmid] < nums[rr]:
                    rr = rmid
                else:
                    return min(self.findMin(nums[rl:rmid+1]), self.findMin(nums[rmid+1:rr+1]))  # bug 越界
            else:
                return nums[rl]
        return nums[rl]     # bug 显示在这

mt = [[2,3,3,0,2], [3,1,2], [1,3,5], [2,2,2,0,1]]
bug = [[3,3,1,3], [1,], [1,1]]
for i in mt+bug:
    print('in:', i)
    print(Solution().findMin(i))