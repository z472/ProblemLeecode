'''
看了力扣的代码，还好没有执着着修改自己丑陋的代码。不知道为啥它居然就是缩小指数的方法就可以解出来
正常的话2.1**3=9.261000000000001，我就考虑字符串去了，然后还要考虑几个不同的情况。
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
它这么写算2.1**3的输出还是得9.261000000000001，不知道这算是什么鬼题
'''
class Solution:
    def myPow(self, x, n):
        # x: float, n: int) -> float:
        rx = repr(x)     # 如果是0.0001，rx为1e-04。之后的index会报错，但是在idle里的话不会这样
        pos_e = rx.find('e')
        if pos_e != -1:
            #  然后一顿改变量，细化下去，这本是repr的问题，却要我来承受
        dot = rx.index('.')
        las = dot
        n_tag = 1 if n >= 0 else -1      # 1 正次幂，-1->负次幂
        for i in range(len(rx)-1, dot, -1):
            if rx[i] != '0':
                las = i
                break
        x = int(rx[:dot]+rx[dot+1:las+1])
        def intPow(ix, n):
            if 2 >= n >= -2:
                return ix**n
            else:
                rem = n % 2
                return intPow(ix, (n-rem)//2)**2*(x**rem)
        output = repr(intPow(x, n*n_tag))
        if n_tag == -1:
            return 10**((dot-las)*n)/int(output)
        leo, bac = len(output), (las-dot)*n
        print(output, las, dot)
        if bac >= leo:
            return float('0.'+'0'*(bac-leo)+output)
        elif bac:
            return float(output[:-bac]+'.'+output[-bac:])
        else:
            return float(output)

a = Solution()
mytest = [(1.2, 2**15), (2.100, 12), (0.03, -2)]
for i in mytest[:]:
    print('in:', i[0], '  ', i[1])
    print(a.myPow(i[0], i[1]))
