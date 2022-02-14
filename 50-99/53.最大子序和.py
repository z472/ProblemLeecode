'''
一次过，运行击败79.67%的Py3提交，占用击败35%。方法就是动态规划，用个accumu变量表示积累值，慢应该是慢
在写法上了。官方的第二种题解是分治，我还没仔细看它是怎么合并起来的，感觉变量挺多挺复杂的
'''
class Solution:
    def maxSubArray(self, nums):
        # nums: List[int]) -> int:
        maxrec, accumu = nums[0], -1
        for i in nums:
            if i > 0:
                if accumu > 0:
                    maxrec = max(i+accumu, maxrec)
                    accumu += i
                else:
                    maxrec = max(i, maxrec)
                    accumu = i
            else:
                maxrec = max(i, maxrec)
                accumu += i
        # print('accumu:', accumu,)
        return maxrec

a = Solution()
mytest = [[-2,1,-3,4,-1,2,1,-5,4], [-1,3,-1,0], [2]]
for i in mytest[:]:
    print('in:', i)
    print(a.maxSubArray(i))