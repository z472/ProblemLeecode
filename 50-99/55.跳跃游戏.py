'''
    这可能是目前为止最快通过的中等难度题了，因为之前遇到过————‘跳跃游戏II’，代码只是在它的基础上加了个
else利用循环。那个代码的写法很优美，技巧之一是：第一个if中的子句修改了该if触发条件的变量，第二个if就是
常规的变量卡位写法。
    这种写法的客观来看就是不用循环嵌套来跳跃，虽然两种写法的运行效率都一样，但是看起来这样用一个for的更
漂亮。
'''
class Solution:
    def canJump(self, nums):
        # nums: List[int]) -> bool:
        maxloc, end = 0, 0
        for i in range(len(nums)):
            if maxloc >= i:
                maxloc = max(maxloc, i+nums[i])
                if i == end:
                    if maxloc >= len(nums)-1:
                        print('i=', i, 'maxloc=', maxloc)
                        return True
                    end = maxloc
            else:
                print('i=', i, 'maxloc=', maxloc)
                return False

a = Solution()
mytest = [[2,3,1,1,4], [2,0,1,0,], [0, ]]
for i in mytest:
    print('in:', i)
    print(a.canJump(i))