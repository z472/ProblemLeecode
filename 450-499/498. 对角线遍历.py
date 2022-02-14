from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        i, j = 0, 0
        # 修改方向
        tag = 0
        for _ in range(m*n):
            res.append(mat[i][j])
            if tag == 0:
                if j == n-1:
                    i += 1
                    tag = 1
                elif i == 0:
                    j += 1
                    tag = 1
                else:
                    i, j = i-1, j+1
            else:
                if i == m-1:
                    j += 1
                    tag = 0
                elif j == 0:
                    i += 1
                    tag = 0
                else:
                    i, j = i+1, j-1
        return res

test = [ [[1,2,3,4],[5,6,7,8],[9,10,11,12]], ]
for i in test:
    print(Solution().findDiagonalOrder(i))



