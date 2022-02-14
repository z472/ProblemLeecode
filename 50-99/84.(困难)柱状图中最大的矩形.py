'''
死于1万多个1组成的列表用例，96个测试项过了87个。
官方题解：复杂度O(n^2)可以根据位序来遍历，也可以根据高度来遍历，你虽然也是根据位序横向遍历的但是你有一个sav列表保存了可能的解，
他们是蛮力法求出该位置的最大值，保存下来，你是每次更新sav中的可能解，然后最后遍历sav计算最大值。由于要更新之前的可能解，故我的
算法也是O(n^2)。虽然复杂度都是过不了大量数据但是相比之下我写的要更复杂和不简洁。     已知的最优解：单调栈。它是从遍历高度优化
延伸来的，有当前的height[i]的值时要向左右寻找第一个比它低的值，而之前遍历过的所有比右边紧挨着的值低的位置都是它的可能解，横坐
标都保存到这个栈中。当遍历到hi时，它看到的栈就是单调递增的（这里应该是严格的不等于），但是保存下的横坐标到height中是单调递增。
然后倒着遍历栈，若高度比hi高的（注意高度相等的也要）就出栈，低的就是hi左边的边界-1的位序，以上两句是这个算法的核心，高的出栈让
低的卡位对后续循环来讲也是正确的，这里值得思考一会。 官方的代码很好理解，这题还是难在方法设计上。  由于每个值的入栈出栈就两个操
作，故为O(n)复杂度。    以下是用两次遍历来分别确定左右边界，但优化的做法是在确定左边界的过程中由于有一个出栈的操作，也就意味着
当前的hi是被出栈位序的右边界，但它算法是高于或等于hi的要出栈这是因为要用后面的位序卡位，反过来说即hi比被弹出对象要小于或是等于，
小于就是右边界，但等于的话应该是要等到hi被踢出时（且是hi高于那时的hi的情况）才能得到右边界。但是由于py3的标签特性，
left[i] = mono_stack[-1] if mono_stack else -1
这句话其实就是可以实现上面传递的功能，因为这是把栈（列表）那个位置给到了left[i]中，它的优化算法是遍历右边界的，然后把原栈最后一个
位置的位序给到左边界，再入栈的。（操作的顺序就像在处理链表）非常细腻专业。
优化单调栈：
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans
未优化单调栈：
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [0] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans
'''


class Solution:
    def largestRectangleArea(self, heights):
        # heights: List[int]) -> int:
        sav = [0] * len(heights)
        ma = 0
        for x, y in enumerate(heights):
            tag = 0
            if x != 0:
                for i in range(x - 1, -1, -1):
                    if sav[i][2] <= y:
                        if not tag and sav[i][2] < y:  # 给比左边矮的位置找左边比它矮的x
                            tag = (i + 1,)
                        if sav[i][1] == x - 1:
                            sav[i][1] += 1
            if x == 0 or heights[x - 1] < y:
                sav[x] = [x, x, y]
            elif heights[x - 1] > y:
                if not tag:
                    sav[x] = [0, x, y]
                else:
                    sav[x] = [tag[0], x, y]
            else:
                sav[x] = sav[x - 1][:]
        # print('sav:', sav)
        for i in sav:
            ma = max((i[1] - i[0] + 1) * i[2], ma)
        return ma


a = Solution()
mt = [[2, 3, 3, 4, 6, 1, 5, 6, ], ]
for i in mt:
    print('in:', i)
    print(a.largestRectangleArea(i))
