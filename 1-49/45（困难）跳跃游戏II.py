'''
    你的方法在面对大的长的数据的时候由于n^2的复杂度会爆炸的。观察的不错，但还有提高的地方。
每个算法都是一个不同的灵魂。这次差了一点点啊。
    它的n^2是贪心，先找到最后一步跳跃前的位置（可能是多个，但是贪心的选择最左边的），找到
最后一步跳跃前所在的位置之后，我们继续贪心地寻找倒数第二步跳跃前所在的位置，以此类推，直到找
到数组的开始位置。（这里选左边仍能得到正确解不会漏解的客观事实是如果能碰到较右的解的时候自然
会先遇到最左边的解）
    虽然我的方法和题解的时间复杂度同为n^2但我时利用一个数组存储然后动态规划的，空间比它还要
大一点。
    最好的时间为n的py3解法如下：编码思路即使是一样的情况下，它的代码也要优美很多，主要是利
用了“多变量卡位”的写法。
    class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
'''
class Solution:
    def jump(self, nums):
        # nums: List[int]) -> int:
        le = len(nums)
        sav = [None]*le
        sav[-1] = 0
        for i in range(le-2, -1, -1):
            lea = -1
            for j in range(1, nums[i]+1):
                if i+j < le and sav[i+j] != -1 and (lea == -1 or lea > sav[i+j]):
                    lea = sav[i+j] + 1
            sav[i] = lea
        print('sav:', sav)
        return sav[0]

a = Solution()
mytest =[[2,3,1,1,4], [2,0,1], ]
lee_test = [[2, 1], ]
for i in lee_test:
    print('hey:', i)
    print(a.jump(i))

