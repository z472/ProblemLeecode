'''
执行用时：60 ms, 在所有 Python3 提交中击败了22.78%的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了5.51%的用户
一次过，但运行表现太菜了。并不是我算法的问题。官方题解tc和sc的最优选，双指针逼近查找。几乎一样的代码，
它用时28ms。比我快了50%多？？？我测了一下它代码，tc 36ms.也比我快了40%之多。
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n-1
        ans = []
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                ans = [left+1, right+1]
                return ans
            elif s > target:
                right -= 1
            else:
                left += 1
        return ans
'''
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1

        while left < right:
            thissum = numbers[left] + numbers[right]
            if thissum == target:
                break
            elif thissum > target:
                right -= 1
            else:
                left += 1
        return [left+1, right+1]

mt = [([2,7,11,15],9), ([2,3,4], 6)]
for i in mt:
    print('in:', repr(i))
    print(Solution().twoSum(i[0], i[1]))