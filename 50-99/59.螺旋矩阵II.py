'''
执行用时：40 ms, 在所有 Python3 提交中击败了58.39%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了47.76%的用户
相比于运行表现，我觉得这次的的代码
if r == rmin+1 and l == lmin:
    rmin, rmax, lmin, lmax = rmin+1, rmax-1, lmin+1, lmax-1
    值得表扬，从事实出发，该处的变量维护写法和简单、很美
'''
class Solution:
    def generateMatrix(self, n):
        # n: int) -> List[List[int]]:
        res = [[None for _ in range(n)] for _ in range(n)]
        rmin, rmax, lmin, lmax = 0, n-1, 0, n-1
        r, l = 0, 0
        for i in range(1, n**2+1):
            res[r][l] = i
            if not r and not l:
                l += 1
            else:
                if r == rmin+1 and l == lmin:
                    rmin, rmax, lmin, lmax = rmin+1, rmax-1, lmin+1, lmax-1
                if r == rmin:   # 右
                    if l == lmax:
                        r += 1
                    else:
                        l += 1
                elif l == lmax: # 下
                    if r == rmax:
                        l -= 1
                    else:
                        r += 1
                elif r == rmax: # 左
                    if l == lmin:
                        r -= 1
                    else:
                        l -= 1
                elif l == lmin: # 上
                    if r == rmin:
                        l += 1
                    else:
                        r -= 1
        return res

a = Solution()
mytest = [3, 5, 10]
for i in mytest:
    print('in:', i)
    for j in a.generateMatrix(i):
        print(j)

