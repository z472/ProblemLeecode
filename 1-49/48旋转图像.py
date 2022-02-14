'''
你比力扣上最简单的思路的效率要低，你运行时间的80%是力扣第一个方法的速度，后面的方法在空间上更加优化
第三种方法是：水平轴翻转，然后沿着主对角线翻转。但它的解释说是一种数值上的偶然。两种翻转实际做的是把
原来的第i行，放到新的倒数第i列（这就是它的第一种解法）这种结果。是一种偶然的数值的巧合。（我开始怀疑自己了）
'''
class Solution:
    def rotate(self, matrix):
        # return: None   matrix: List[List[int]]
        n = len(matrix[0])
        sav = [None]*(n-1)
        cou = 0
        while cou < n-1:
            sav[:n-cou] = matrix[cou][cou:n-1]
            print('sav:', sav)
            for i in range(4):
                sta = cou if i < 2 else n-1
                for mov in range(0, n-1-cou):
                    if i == 0:
                        matrix[sta][cou+mov] = matrix[n-1-mov][sta]
                    elif i == 1:
                        matrix[n-1-mov][sta] = matrix[n-1][n-1-mov]
                    elif i == 2:
                        matrix[sta][sta-mov] = matrix[cou+mov][sta]
                    elif i == 3:
                        matrix[cou+mov][sta] = sav[mov]
            cou, n = cou+1, n-1
        print(matrix)

a = Solution()
mytest = ([[1,2],[3,4]], [[5,1,9,11,20],[2,4,8,10,19],[13,3,6,7,22],[15,14,12,16,23],[17,18,21,25,24]])
for i in mytest:
    print('matrix:',i)
    a.rotate(i)
