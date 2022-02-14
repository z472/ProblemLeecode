class Solution:
    def solveNQueens(self, n):
        # n: int) -> List[List[str]]:
        sav = [['.' for _ in range(n)] for _ in range(n)]   # 动态维护
        print(id(sav))
        row = [i for i in range(n)]     # 可以填的行位置
        lin = [i for i in range(n)]     # 可以填的列位置
        res = []
        print(id(res))
        def child(r, l):
            if r in row and l in lin:
                for tr in range(r):
                    tl = sav[tr].index('Q')
                    if tr-r == tl-l or tr-r == l-tl:
                        return -1   # 不符合斜向的约束
                if r == n-1:
                    sav[r][l] = 'Q'
                    print('this sav :', sav)
                    print(id(sav))
                    res.append(sav[:])
                    print('?', sav[:])
                    print('?id sav[:]', id(sav[:]))
                    print('?id sav[:]', id(sav[:]))
                    print('that res:', res)
                    print(id(res))
                    sav[r][l] = '.'
                    return 0

                sav[r][l] = 'Q'
                row.remove(r)
                lin.remove(l)

                for i in range(n):
                    child(r+1, i)

                if r+1 in row:
                    row.append(r)
                    lin.append(l)
                    sav[r][l] = '.'
                    return -1
            return -1   # 不符合行列的判断
        for i in range(n):
            child(0, i)
        print('res[0] out id ', id(res[0]))
        print('res[1] out id ', id(res[1]))
        print('res out id ', id(res))
        return res

a = Solution()
mytest = [4, ]
for x in mytest:
    print('in:', x)
    # print(len(a.solveNQueens(x)))
    for i, j in enumerate(a.solveNQueens(x)):
        print(i, '  ', j)

