from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]):
        # 由于除法优先级这个东西，不知道怎么处理，而且输入数量n为0-10
        # 故绝对采取dp蛮力法计算出某长度的最大值，比如长度1-n的最大值
        # 遍历max(1--i) / min(i+1 -- 4) i从1到n-1都计算一遍得到
        # 最大的值，因为显然要求某段的最小值，故每个dp位置是要保持这两个
        # 值。但注意题目要输出为没有冗余括号的字符串。
        le = len(nums)
        # 注意这个矩阵的初值是从对角线位置开始走的，但由于它dp计算的方式
        # 还是不能转成一维数组来处理
        dp = [[[nums[j], nums[j]] if j == i else [0, 0] for j in range(le)] for i in range(le)]

        def cal(x, y):
            rmax, rmin = float('-inf'), float('inf')
            for i in range(x, y):
                rmax = max(rmax, nums[x][i][0] / nums[i + 1][y][1])
                rmin = min(rmin, nums[x][i][1] / nums[i + 1][y][0])
            return [rmax, rmin]

        for start in range(1, le):
            i, j = start, 0
            for offsettimes in range(0, le - start):
                nums[i][j] = cal(i, j)
                i, j = i+1, j+1

'''
上面的算法可行，但是后续还要去掉冗余的括号，整个过程就很麻烦了。(中等题不会这么麻烦，就算会也是方法不好)
所以我直接跳向题解，最后那个算法说是数学，其实就是利用到一些事实所做的最棒解法。

首先要回顾一个小学数学知识，a/b/c = a/c/b = a/(b*c)。我忘记了这个东西，所以上面说不知道如何处理连除的
优先级。下面是一些原则，a1/a2/a3/../an这个序列不论怎么加括号a1必做分子，更重要的是a2必做分母。
故最好的情况就是(a1*a3*a4*...*an)/a2。结合小学数学知识和 a/(b/c)=(a*c)/b 就是在a2开始括号直到an。

由于那个xx数学知识，故可以对括号做一个理解：它固定了被括内容序列的前两个值的相对关系，必是a1/a2。
'''