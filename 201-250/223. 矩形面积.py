'''
执行用时：72 ms, 在所有 Python3 提交中击败了12.53%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了62.91%的用户
这题有别的更好的解法？无官方题解。下面是40ms,超过99.4%提交的代码。这道题居然有3080个测试用例。
比较一下代码很容易发现，确实写的有冗余的地方，为啥要保存那些值到outrectanble四元组里呢？这，败笔。

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area_total = abs((C-A)*(D-B))+abs((H-F)*(G-E))
        if B >= H or D <= F or C <= E or G<=A:
            return area_total
        S = abs((min(D,H)-max(B,F))*(min(C,G)-max(A,E)))
        return area_total-S
'''
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        # （A,B),(C,D);(E,F),(G,H)
        outrectangle = (max(A, E), min(C, G), max(B, F), min(D, H))
        overlaparea = 0
        if outrectangle[0] <= outrectangle[1] and outrectangle[2] <= outrectangle[3]:
            overlaparea =  (outrectangle[1] - outrectangle[0]) * (outrectangle[3] - outrectangle[2])
        return (A-C)*(B-D)+(E-G)*(F-H)-overlaparea


mt = [(-3,0,3,4,0,-1,9,2)]
x = mt[0]
print(Solution().computeArea(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))