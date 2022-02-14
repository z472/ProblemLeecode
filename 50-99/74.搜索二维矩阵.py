'''
执行用时：44 ms, 在所有 Python3 提交中击败了33.30%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了32.03%的用户
第二次过的，对行首值进行二分查找，然后对目标行进行二分查找。
代码：二分查找下取整或是上取整都是会有一个边界值会漏掉判断，然后
就是循环跳出，每次让二分值的位置+1或-1，而不是用原值做边界。

官方题解：把所有数都考虑进去，每次也是确定一个中值，然后二分法去
判断缩小范围。但它的中值是个数的中间值，起始两端是0，m*n-1，由
中值整除n得到在第几行，中值取余n确定在第几列。复杂度虽然和我一样
是log(mn),但它不论是代码的长度，变量的个数，边界值的判断都比我要
更好。而且鉴于以上原因肯定比我更快些。
'''
class Solution:
    def searchMatrix(self, matrix, target):
        # matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, m - 1
        # 超出范围返回错误
        if matrix[0][0] > target or matrix[m - 1][n - 1] < target:
            return False
        while j - i > 1:
            if matrix[(i + j) // 2][0] == target:
                return True
            if matrix[(i + j) // 2][0] < target:
                i = (i + j) // 2
            else:
                j = (i + j) // 2
        if matrix[m - 1][0] <= target:
            i = j
        sav = i
        print('sav=', sav)
        i, j = 0, n - 1
        while j > i:
            if matrix[sav][(i + j) // 2] == target:
                return True
            elif matrix[sav][(i + j) // 2] < target:
                i = (i + j) // 2 + 1
            else:
                j = (i + j) // 2 - 1
        return True if matrix[sav][i] == target else False


a = Solution()
mt = [([[1, 3, 5, 7], [10, 12, 16, 20], [24, 30, 34, 60]]), [[1, 3]]]
for i in mt[:1]:
    print('in:', i)
    for j in [7, 20, 60, 8, 22]:
        print('j=', j)
        print(a.searchMatrix(i, j))
