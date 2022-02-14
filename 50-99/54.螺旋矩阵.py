'''
    丑陋到极致的写法。思路是先把matrix[0][0]和[0][1]给到输出里，把matrix[0][1]到循环中然后四种变向
tag表示一种方向，变向就+1，增加位序，循环靠着数值横向纵向乘积-2作为终止，还要维护着横纵的边界值，每次
变向相应变更一下。
    运行超过98.38%的py3提交，占用超过5%（几乎是垫底了）。最恶心我的是这种写法。还遇到了一个维护边界值的
错误。我大意了。
    说实话到通过我觉得自己没有一点提升，因为这种难度的话应该速度解决的，但我出了一个错误而且代码的编写让人
作呕。     看了两种官方题解，都是很长的虽然重复度没我这么高但并没有什么本质的不同，主要咱也没利用额外的空间
存储输出矩阵。复杂度为O(1).
'''
class Solution:
    def spiralOrder(self, matrix):
        # matrix: List[List[int]]) -> List[int]:
        r_high, r_low, l_left, l_right = 0, len(matrix)-1, 0, len(matrix[0])-1
        if len(matrix[0]) == 1:
            return [matrix[i][0] for i in range(len(matrix))]
        r, l, tag = 0, 1, 0
        res = [matrix[0][0], matrix[0][1]]
        for _ in range(len(matrix)*len(matrix[0])-2):
            if tag == 0 and l == l_right:
                r_high += 1
                tag = (tag+1)%4
            elif tag == 1 and r == r_low:
                l_right -= 1
                tag = (tag+1)%4
            elif tag == 2 and l == l_left:
                r_low -= 1
                tag = (tag+1)%4
            elif tag == 3 and r == r_high:
                l_left += 1
                tag = (tag+1)%4
            if tag == 0:
                l += 1
            elif tag == 1:
                r += 1
            elif tag == 2:
                l -= 1
            elif tag == 3:
                r -= 1
            # print(matrix[r][l])
            res.append(matrix[r][l])
        return res

a = Solution()
mytest = ([[1,2,], [4,5,], [7,8,]], [[0],[1],[2],[3]], [[1,2,3,4], [5,6,7,8]], [[1,2,3]])
for i in mytest[1:]:
    print('in:')
    for j in i:
        print(j)
    print(a.spiralOrder(i))
