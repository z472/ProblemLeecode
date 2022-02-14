'''
执行用时：64 ms, 在所有 Python3 提交中击败了27.33%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了80.22%的用户
之前一直有看的 计数字典 结构。主动使用。但这题很一般。注意两个Counter之中的交集。确实是数学概念的。
如果一个字典里没有是不算进去的。无官方题解，下面看一个32ms，击败100%，且也是用计数字典的代码。

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 公牛：数+要考虑位置
        # 奶牛：数+不考虑位置
        res = ''
        bulls = 0
        d1 = collections.Counter(secret)
        d2 = collections.Counter(guess)
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
        cows = 0
        # print(d1,d2)
        for k1 in d1.keys():
            if k1 in d2.keys():
                cows+=min(d1[k1],d2[k1])
        cows = cows-bulls
        return str(bulls)+'A'+str(cows)+'B'
我的取交集也是 min(d1[k1], d2[k1])。主要的区别是我每次发现bulls就减少两个字典的对应的值。为了不干扰后续。
它是不管，然后 cows -= bulls
'''
from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secdict = Counter(secret)
        guedict = Counter(guess)
        bulls, cows = 0, 0
        for i, j in zip(secret, guess):
            if i == j:
                secdict[i] -= 1
                guedict[j] -= 1
                bulls += 1
        c = secdict & guedict
        for i in c:
            cows += c[i]
        return str(bulls) + 'A' + str(cows) + 'B'

mt = [('1807','7810'),('1123','0111'), ('2235', '1122')]
for i in mt:
    print(repr(i))
    print(Solution().getHint(i[0], i[1]))

