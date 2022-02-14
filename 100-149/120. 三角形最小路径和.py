'''
执行用时：44 ms, 在所有 Python3 提交中击败了75.86%的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了45.54%的用户
第一次居然错在了重大的逻辑上，找了半天，第二次过了。简单的DP,和之前的一些最优解的题一样，类似64和70题类似。
就像考试的时候会的题答不对那味了。   官方题解里空间最少的就是我这个意思。但它在写的时候避开了我出bug的点，
res[j]会覆盖之后，下次算j+1位置就看不到上一层j的值了。它是倒着算，从右向左遍历，修改的是最后一个，不影响
下次遍历。可以说是利用了上下层错位的现象。   最骚的是还有在输入数组里DP的，还有从底层向上层DP的。    而且
这也是一道经典的题，最早出现在1994的IOI（国际信息学奥林匹克竞赛）的 The Triangle。现在成为一个入门题。
官方题解：不断督促着我们学习和巩固算法。
'''
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        le = len(triangle)
        if le == 1:
            return triangle[0][0]
        res = [triangle[0][0]]
        for i in range(1, le):  # le行，第i行
            pre = res[0]
            for j in range(i + 1):
                if j == 0:
                    res[j] += triangle[i][j]
                elif j <= i-1:
                    x, pre = min(pre, res[j]), res[j]
                    res[j] = x + triangle[i][j]
                else:
                    res.append(pre + triangle[i][j])

        print(res)
        return min(res)


mt = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
leet = [[-7],[-2,1],[-5,-5,9],[-4,-5,4,4],[-6,-6,2,-1,-5],[3,7,8,-3,7,-9],
        [-9,-1,-9,6,9,0,7],[-7,0,-6,-8,7,1,-4,9],[-3,2,-6,-9,-7,-6,-9,4,0],
        [-8,-6,-3,-9,-2,-6,7,-5,0,7],[-9,-1,-2,4,-2,4,4,-1,2,-5,5],
        [1,1,-6,1,-2,-4,4,-2,6,-6,0,6],[-3,-3,-6,-2,-6,-2,7,-9,-5,-7,-5,5,1]]
Solution().minimumTotal(leet[:])
