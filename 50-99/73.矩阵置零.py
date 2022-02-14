class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        一个直接的解决方案是使用 O(mn)的额外空间，但这并不是一个好的解决方案。
        一个简单的改进方案是使用 O(m+n) 的额外空间，但这仍然不是最好的解决方案。
        你能想出一个常数空间的解决方案吗？
        matrix: List[List[int]]) -> None
        执行用时：40 ms, 在所有 Python3 提交中击败了95.86%的用户
        内存消耗：15.3 MB, 在所有 Python3 提交中击败了12.85%的用户

        提交：错了三次，全是修改代码，然后逻辑出问题了。挺蠢的。改的写的
        过程也不是很享受，很折磨，if..elif和if..if，tag%2那里的判断
        等等，很多都是完全写反了。

        我的算法：把横列的记录放在第一行和第一列中，然后就是处理各种纠缠在
        一起的各种情况。具体实现先是1-遍历：遍历非No.1行或是列，修改到该行
        或列所对应的第一行或列值改成0；遍历第一行或是第一列的时候修改tag来
        记录各自是否要全部置0，这里利用了乘法的特性具体实现标记的。 2-修改
        非第一行列的值依据第一行列的0来修改即可，第一行列依据tag来修改。

        官方题解：常数空间的算法（只是在记录第一行列是否置零的操作比我更简单优美）
        遍历整个矩阵，如果 cell[i][j] == 0 就将第 i 行和第 j 列的第一个元素标记。
        第一行和第一列的标记是相同的，都是 cell[0][0]，所以需要一个额外的变量告知第
        一列是否被标记，同时用 cell[0][0] 继续表示第一行的标记。（它这里的处理比我
        好很多，省去了很多判断和特例化代码）
        """
        m, n = len(matrix), len(matrix[0])
        tag = 1
        if matrix[0][0] == 0:
            tag *= 6
        if m == 1 and 0 in matrix[0]:
            for i in range(n):
                matrix[0][i] = 0
        if n == 1 and [0] in matrix:
            for i in range(m):
                matrix[i][0] = 0
        if m == 1 or n == 1:
            return None
        for i in range(m):
            for j in range(n):
                if i == 0 and matrix[0][j] == 0 and (tag % 2 != 0 or tag == 1):
                    tag *= 2
                elif j == 0 and matrix[i][0] == 0 and (tag % 3 != 0 or tag == 1):
                    tag *= 3
                elif (matrix[i][0] or matrix[0][j]) and matrix[i][j] == 0:
                    matrix[0][j], matrix[i][0] = 0, 0
        print('tag=', tag)
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for i in range(1, n):
            if matrix[0][i] == 0:
                for j in range(1, m):
                    matrix[j][i] = 0
        if not tag % 2:
            for i in range(n):
                matrix[0][i] = 0
        if not tag % 3:
            for i in range(m):
                matrix[i][0] = 0
        return None

# 上面代码不能直接测试（还要改输出），那是提交的答案
a = Solution()
mt = (
    [[1, 1, 1], [1, 0, 1], [1, 1, 2]], [[1, 1, 2, 3], [1, 4, 0, 2], [0, 3, 1, 5]], [[0], [1], [3], [3]], [[1, 2, 0, 4]])
leet = ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]])
for i in leet[:]:
    print('in:', )
    for j in i:
        print(j)
    print('out:')
    for j in a.setZeroes(i):
        print(j)
    print('')
