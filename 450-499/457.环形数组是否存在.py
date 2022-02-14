'''
tc = O(n^2)但我是纯的sc = O(1)。
看了官方题解，sc=O(1)很尬，它是在原数组上修改，却没说可以这样弄，我没动它所以得反复遍历，其他逻辑都对的。

就是快慢指针，快的为慢的2倍最后会相遇到，这之中有一些限制逻辑不要写错了。
'''
from typing import List
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        lenums = len(nums)
        mv = lambda x:(x+nums[x])%lenums
        # print('0:', mv(0))
        for start in range(lenums):
            a = b = start
            for _ in range(lenums):
                if nums[a]*nums[mv(a)] < 0 or nums[mv(a)] * nums[mv(mv(a))] < 0 or mv(a) == mv(mv(a)):
                    break
                a = mv(mv(a))
                print('a=',a)
                b = mv(b)
                print('b=',b)
                if a == b:
                    print('T:',a,'start:',start)
                    return True
        print('单纯的无法循环')
        return False


test = [[-2, 1, -1, -2, -2], [3,1,2],[1,1,1,1,1,1,1,1,1,-5]]
# FTF
for i in test[-1:]:
    print('————————————\n',i)
    print(Solution().circularArrayLoop(i))