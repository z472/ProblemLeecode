'''
执行用时：2092 ms, 在所有 Python3 提交中击败了7.72%的用户
内存消耗：17.3 MB, 在所有 Python3 提交中击败了5.01%的用户

我虽然是对代码运行表现没有要求的人，但是这也太慢了吧。看下别的题解。
为啥官方也是单调栈+什么东西弄的，

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [-1] * n
        stk = list()

        for i in range(n * 2 - 1):
            while stk and nums[stk[-1]] < nums[i % n]:
                ret[stk.pop()] = nums[i % n]
            stk.append(i % n)

        return ret
人家是82ms，同样的测试用例哦，我炸了。可以看到循环和你写的挺像的。
'''
from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        numslen = len(nums)
        def looplen(list):
            for i in range(1, numslen+1):
                if numslen // i > 1 and list[:numslen] == list[numslen:2*numslen]:
                    return i
                if list[:numslen%i] == list[i:]:
                    return i
            return numslen
        looplenth = looplen(nums)
        print('len:', looplenth)

        res = [-1 for _ in range(looplenth)]
        stack = [[0,nums[0]]]
        for i in range(1,2*looplenth):
            while stack and nums[i%looplenth] > stack[-1][1]:
                resi, resval = stack.pop()
                res[resi] = nums[i%looplenth]
            stack.append([i%looplenth, nums[i%looplenth]])

        return res * (numslen // looplenth) + res[:numslen%looplenth]

test = [[1,2,3,4,3],]
for i in test:
    print(Solution().nextGreaterElements(i))